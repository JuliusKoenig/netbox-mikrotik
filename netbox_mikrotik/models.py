from django.db import models
from django.utils.translation import gettext_lazy as _
from ipam.models import IPAddress
from netbox.models import NetBoxModel


class MikrotikDevice(NetBoxModel):
    device = models.OneToOneField(
        verbose_name=_("Device"),
        to="dcim.Device",
        on_delete=models.PROTECT,
        related_name="netbox_mikrotik_mikrotik_device",
    )
    foo = models.CharField(max_length=50)
    bar = models.CharField(max_length=50)

    class Meta:
        db_table = "netbox_mikrotik_device"
        verbose_name = _("Device")
        verbose_name_plural = _("Devices")
        ordering = ["device__name"]

    def __str__(self):
        return f'{self.foo} {self.bar}'

    @property
    def str(self) -> str:
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
