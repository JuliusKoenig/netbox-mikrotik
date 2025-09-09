from netbox.forms import NetBoxModelForm

from netbox_mikrotik.models import MikrotikDevice


class MikrotikDeviceForm(NetBoxModelForm):
    class Meta:
        model = MikrotikDevice
        fields = [
            "device",
            "foo",
            "bar"
        ]
