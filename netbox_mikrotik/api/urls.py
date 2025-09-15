from netbox.api.routers import NetBoxRouter

from netbox_mikrotik.api.views import MikrotikDeviceViewSet, SyncGroupViewSet

app_name = "netbox_mikrotik"

router = NetBoxRouter()
router.register("device", MikrotikDeviceViewSet)
router.register("syn-group", SyncGroupViewSet)
urlpatterns = router.urls
