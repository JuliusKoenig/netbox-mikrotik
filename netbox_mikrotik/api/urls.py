from netbox.api.routers import NetBoxRouter

from netbox_mikrotik.api.views import MikrotikDeviceViewSet

app_name = "netbox_mikrotik"

router = NetBoxRouter()
router.register("device", MikrotikDeviceViewSet)
urlpatterns = router.urls
