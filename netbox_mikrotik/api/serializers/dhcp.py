from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from netbox_mikrotik.models import MikrotikDhcpServer, MikrotikDhcpLease

__all__ = ("MikrotikDhcpServerSerializer", "MikrotikDhcpLeaseSerializer")


class MikrotikDhcpServerSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:netbox_mikrotik-api:mikrotikdhcpserver-detail")

    class Meta:
        model = MikrotikDhcpServer
        fields = ["id",
                  "created",
                  "last_updated",
                  "custom_field_data",
                  "mikrotik_device",
                  "name"]
        brief_fields = (
            "id",
            "mikrotik_device",
            "name"
        )

    name = serializers.CharField(read_only=True)


class MikrotikDhcpLeaseSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:netbox_mikrotik-api:mikrotikdhcpserver-detail")

    class Meta:
        model = MikrotikDhcpLease
        fields = ["id",
                  "created",
                  "last_updated",
                  "custom_field_data",
                  "mikrotik_dhcp_server",
                  "mac_address"]
        brief_fields = (
            "id",
            "mikrotik_dhcp_server",
            "mac_address"
        )
