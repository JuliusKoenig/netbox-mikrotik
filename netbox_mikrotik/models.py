from django.db.models import CharField, OneToOneField, BooleanField, DateTimeField, CASCADE
from django.utils.translation import gettext_lazy as _
from ipam.models import IPAddress
from netbox.models import NetBoxModel


class MikrotikDevice(NetBoxModel):
    device = OneToOneField(
        verbose_name=_("Device"),
        to="dcim.Device",
        on_delete=CASCADE,
        related_name="netbox_mikrotik_mikrotik_device",
    )
    username = CharField(max_length=64, null=False, blank=False)
    password = CharField(max_length=254, null=False, blank=False)
    address_list_sync = BooleanField(default=False)
    dns_sync = BooleanField(default=False)
    dhcp_sync = BooleanField(default=False)
    last_run = DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "netbox_mikrotik_device"
        verbose_name = _("Device")
        verbose_name_plural = _("Devices")
        ordering = ["device__name"]

    def __str__(self):
        return f"Mikrotik {_('Device')} - {self.device.name}"

    @property
    def name(self) -> str:
        return str(self)

    @property
    def ip_address(self) -> IPAddress | None:
        if self.device.primary_ip4:
            return self.device.primary_ip4
        if self.device.primary_ip6:
            return self.device.primary_ip6
        for interface in self.device.interfaces.all():
            for ip in interface.ip_addresses.all():
                return ip
        return None
