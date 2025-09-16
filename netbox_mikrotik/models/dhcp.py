from django.db.models import CharField, ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _
from netbox.models import NetBoxModel

__all__ = ("MikrotikDhcpServer", "MikrotikDhcpLease")


class MikrotikDhcpServer(NetBoxModel):
    mikrotik_device = ForeignKey(
        verbose_name=_("Mikrotik Device"),
        to="netbox_mikrotik.MikrotikDevice",
        on_delete=CASCADE,
        related_name="mikrotik_dhcp_servers",
        null=False,
        blank=False
    )
    name = CharField(max_length=64, null=False, blank=False)

    class Meta:
        db_table = "netbox_mikrotik_dhcp_server"
        verbose_name = _("DHCP Server")
        verbose_name_plural = _("DHCP Servers")
        ordering = ["name"]

    def __str__(self):
        return self.name


class MikrotikDhcpLease(NetBoxModel):
    mikrotik_dhcp_server = ForeignKey(
        verbose_name=_("Mikrotik DHCP Server"),
        to="netbox_mikrotik.MikrotikDhcpServer",
        on_delete=CASCADE,
        related_name="netbox_mikrotik_dhcp_leases",
        null=False,
        blank=False
    )
    mac_address = ForeignKey(
        verbose_name=_("MAC Address"),
        to="dcim.MACAddress",
        on_delete=CASCADE,
        related_name="netbox_mikrotik_dhcp_leases",
        null=False,
        blank=False
    )

    class Meta:
        db_table = "netbox_mikrotik_dhcp_lease"
        verbose_name = _("DHCP Lease")
        verbose_name_plural = _("DHCP Leases")
        ordering = ["mac_address"]

    def __str__(self):
        return f"{self.mikrotik_dhcp_server.name} - {self.mac_address}"
