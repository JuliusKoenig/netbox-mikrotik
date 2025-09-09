from django.urls import include, path
from utilities.urls import get_model_urls

from netbox_mikrotik.views import *  # noqa: F401

app_name = "netbox_mikrotik"

urlpatterns = [path("devices/",
                    include(get_model_urls(app_name, "mikrotikdevice", detail=False))),
               path("devices/<int:pk>/",
                    include(get_model_urls(app_name, "mikrotikdevice")))]
