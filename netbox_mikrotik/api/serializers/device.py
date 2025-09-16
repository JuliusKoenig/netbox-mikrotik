from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from netbox_mikrotik.models import MikrotikDevice

__all__ = ("MikrotikDeviceSerializer",)


class MikrotikDeviceSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:netbox_mikrotik-api:mikrotikdevice-detail")

    class Meta:
        model = MikrotikDevice
        fields = ["id",
                  "created",
                  "last_updated",
                  "custom_field_data",
                  "name",
                  "ip_address",
                  "username",
                  "password",
                  "address_list_sync",
                  "dns_sync",
                  "dhcp_sync",
                  "last_run",
                  "device"]
        brief_fields = (
            "id",
            "name",
            "ip_address"
        )

    name = serializers.CharField(read_only=True)
    ip_address = serializers.IPAddressField(read_only=True)
    password = serializers.CharField(write_only=True)
    last_run = serializers.DateTimeField(read_only=True)
