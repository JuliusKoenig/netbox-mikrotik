from netbox.api.routers import NetBoxRouter

from netbox_mikrotik.api.views import MikrotikDeviceViewSet, MikrotikDhcpServerViewSet, MikrotikDhcpLeaseViewSet

app_name = "netbox_mikrotik"

router = NetBoxRouter()
router.register("device", MikrotikDeviceViewSet)
router.register("dhcp-server", MikrotikDhcpServerViewSet)
router.register("dhcp-lease", MikrotikDhcpLeaseViewSet)
urlpatterns = router.urls
