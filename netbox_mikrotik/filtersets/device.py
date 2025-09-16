from netbox.filtersets import NetBoxModelFilterSet

from netbox_mikrotik.models import MikrotikDevice

__all__ = ("MikrotikDeviceFilterSet",)


class MikrotikDeviceFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = MikrotikDevice
        fields = ("id",)
