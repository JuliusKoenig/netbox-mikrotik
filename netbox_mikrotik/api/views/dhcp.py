from netbox.api.viewsets import NetBoxModelViewSet

from netbox_mikrotik.models import MikrotikDhcpServer, MikrotikDhcpLease
from netbox_mikrotik.api.serializers import MikrotikDhcpServerSerializer, MikrotikDhcpLeaseSerializer

__all__ = ("MikrotikDhcpServerViewSet", "MikrotikDhcpLeaseViewSet")


class MikrotikDhcpServerViewSet(NetBoxModelViewSet):
    queryset = MikrotikDhcpServer.objects.all()
    serializer_class = MikrotikDhcpServerSerializer
    # filterset_class = filtersets.FloorplanFilterSet # ToDo


class MikrotikDhcpLeaseViewSet(NetBoxModelViewSet):
    queryset = MikrotikDhcpLease.objects.all()
    serializer_class = MikrotikDhcpLeaseSerializer
    # filterset_class = filtersets.FloorplanFilterSet # ToDo
