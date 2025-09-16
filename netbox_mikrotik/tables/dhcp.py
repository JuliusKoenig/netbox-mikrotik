from django_tables2 import LinkColumn
from django.utils.translation import gettext_lazy as _
from netbox.tables import NetBoxTable, ToggleColumn

from netbox_mikrotik.models import MikrotikDhcpServer, MikrotikDhcpLease

__all__ = ("MikrotikDhcpServerTable", "MikrotikDhcpLeaseTable")


class MikrotikDhcpServerTable(NetBoxTable):
    pk = ToggleColumn()
    mikrotik_device = LinkColumn(verbose_name=_("Mikrotik Device"))
    name = LinkColumn(verbose_name=_("Name"))

    class Meta(NetBoxTable.Meta):
        model = MikrotikDhcpServer
        fields = (
            "pk",
            "mikrotik_device",
            "name",
            "actions"
        )
        default_columns = (
            "mikrotik_device",
            "name",
            "actions"
        )


class MikrotikDhcpLeaseTable(NetBoxTable):
    pk = ToggleColumn()
    mikrotik_dhcp_server = LinkColumn(verbose_name=_("Mikrotik DHCP Server"))
    mac_address = LinkColumn(verbose_name=_("MAC Address"))

    class Meta(NetBoxTable.Meta):
        model = MikrotikDhcpLease
        fields = (
            "pk",
            "mikrotik_dhcp_server",
            "mac_address",
            "actions"
        )
        default_columns = (
            "mikrotik_dhcp_server",
            "mac_address",
            "actions"
        )
