from django.urls import include, path
from utilities.urls import get_model_urls

from netbox_mikrotik.views import *  # noqa: F401

app_name = "netbox_mikrotik"

urlpatterns = [path("dhcp-servers/",
                    include(get_model_urls(app_name, "mikrotikdhcpserver", detail=False))),
               path("dhcp-servers/<int:pk>/",
                    include(get_model_urls(app_name, "mikrotikdhcpserver"))),
               path("dhcp-leases/",
                    include(get_model_urls(app_name, "mikrotikdhcplease", detail=False))),
               path("dhcp-leases/<int:pk>/",
                    include(get_model_urls(app_name, "mikrotikdhcplease"))),
               path("devices/",
                    include(get_model_urls(app_name, "mikrotikdevice", detail=False))),
               path("devices/<int:pk>/",
                    include(get_model_urls(app_name, "mikrotikdevice")))]
