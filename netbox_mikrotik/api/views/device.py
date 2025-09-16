from netbox.api.viewsets import NetBoxModelViewSet

from netbox_mikrotik.models import MikrotikDevice
from netbox_mikrotik.api.serializers import MikrotikDeviceSerializer

__all__ = ("MikrotikDeviceViewSet",)


class MikrotikDeviceViewSet(NetBoxModelViewSet):
    queryset = MikrotikDevice.objects.all()
    serializer_class = MikrotikDeviceSerializer
    # filterset_class = filtersets.FloorplanFilterSet # ToDo
