from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from netbox_mikrotik.models import MikrotikDevice


class MikrotikDeviceSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:netbox_mikrotik-api:mikrotikdevice-detail")

    class Meta:
        model = MikrotikDevice
        fields = ["id",
                  "foo",
                  "bar",
                  "device_id",
                  "created",
                  "last_updated"]
        brief_fields = ["id",
                        "foo",
                        "bar",
                        "device_id"]
