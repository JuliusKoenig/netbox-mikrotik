from django.forms import PasswordInput
from netbox.forms import NetBoxModelForm

from netbox_mikrotik.models import MikrotikDevice, SyncGroup


class MikrotikDeviceForm(NetBoxModelForm):
    class Meta:
        model = MikrotikDevice
        fields = [
            "device",
            "username",
            "password",
            "address_list_sync",
            "dns_sync",
            "dhcp_sync",
            "sync_groups"
        ]
        widgets = {
            'password': PasswordInput(render_value=True),
        }

class SyncGroupForm(NetBoxModelForm):
    class Meta:
        model = SyncGroup
        fields = [
            "name",
            "tenants"
        ]
