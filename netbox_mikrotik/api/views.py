from netbox.api.viewsets import NetBoxModelViewSet

from netbox_mikrotik.models import MikrotikDevice, SyncGroup
from netbox_mikrotik.api.serializers import MikrotikDeviceSerializer, SyncGroupSerializer


class MikrotikDeviceViewSet(NetBoxModelViewSet):
    queryset = MikrotikDevice.objects.all()
    serializer_class = MikrotikDeviceSerializer
    # filterset_class = filtersets.FloorplanFilterSet # ToDo

class SyncGroupViewSet(NetBoxModelViewSet):
    queryset = SyncGroup.objects.all()
    serializer_class = SyncGroupSerializer
    # filterset_class = filtersets.FloorplanFilterSet # ToDo
