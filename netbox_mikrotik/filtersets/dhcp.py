from netbox.filtersets import NetBoxModelFilterSet

from netbox_mikrotik.models import MikrotikDhcpServer, MikrotikDhcpLease

__all__ = ("MikrotikDhcpServerFilterSet", "MikrotikDhcpLeaseFilterSet")


class MikrotikDhcpServerFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = MikrotikDhcpServer
        fields = ("id",)


class MikrotikDhcpLeaseFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = MikrotikDhcpLease
        fields = ("id",)
