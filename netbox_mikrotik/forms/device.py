from django.forms import PasswordInput
from netbox.forms import NetBoxModelForm

from netbox_mikrotik.models import MikrotikDevice

__all__ = ("MikrotikDeviceForm",)


class MikrotikDeviceForm(NetBoxModelForm):
    class Meta:
        model = MikrotikDevice
        fields = [
            "device",
            "username",
            "password",
            "address_list_sync",
            "dns_sync",
            "dhcp_sync"
        ]
        widgets = {
            "password": PasswordInput(render_value=True),
        }
