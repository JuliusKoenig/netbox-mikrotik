from django.utils.translation import gettext_lazy as _
from netbox.views.generic import ObjectView
from utilities.views import register_model_view, ViewTab
from dcim.models import Device

__all__ = ()


@register_model_view(Device, name="mikrotik")
class DeviceMikrotikView(ObjectView):
    queryset = Device.objects.all()
    template_name = "netbox_mikrotik/device/mikrotik.html"
    tab = ViewTab(
        label=_("Mikrotik"),
        hide_if_empty=True,
    )
