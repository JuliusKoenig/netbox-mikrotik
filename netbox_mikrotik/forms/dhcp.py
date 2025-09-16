from netbox.forms import NetBoxModelForm

from netbox_mikrotik.models import MikrotikDhcpServer, MikrotikDhcpLease

__all__ = ("MikrotikDhcpServerForm", "MikrotikDhcpLeaseForm")


class MikrotikDhcpServerForm(NetBoxModelForm):
    class Meta:
        model = MikrotikDhcpServer
        fields = [
            "mikrotik_device",
            "name"
        ]


class MikrotikDhcpLeaseForm(NetBoxModelForm):
    class Meta:
        model = MikrotikDhcpLease
        fields = [
            "mikrotik_dhcp_server",
            "mac_address"
        ]
