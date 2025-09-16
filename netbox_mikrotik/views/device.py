from netbox.views.generic import ObjectListView, ObjectView, ObjectEditView, ObjectDeleteView, BulkImportView, \
    BulkEditView, BulkDeleteView
from utilities.views import register_model_view

from netbox_mikrotik.models import MikrotikDevice
from netbox_mikrotik.tables import MikrotikDeviceTable
from netbox_mikrotik.filtersets import MikrotikDeviceFilterSet
from netbox_mikrotik.forms import MikrotikDeviceForm

__all__ = ("MikrotikDeviceListView",
           "MikrotikDeviceView",
           "MikrotikDeviceEditView",
           "MikrotikDeviceDeleteView",
           "MikrotikDeviceBulkImportView",
           "MikrotikDeviceBulkEditView",
           "MikrotikDeviceBulkDeleteView")


@register_model_view(MikrotikDevice, "list", path="", detail=False)
class MikrotikDeviceListView(ObjectListView):
    queryset = MikrotikDevice.objects.all()
    filterset = MikrotikDeviceFilterSet
    # filterset_form = MikrotikDeviceForm ' ToDo
    table = MikrotikDeviceTable


@register_model_view(MikrotikDevice)
class MikrotikDeviceView(ObjectView):
    queryset = MikrotikDevice.objects.all()


@register_model_view(MikrotikDevice, "add", detail=False)
@register_model_view(MikrotikDevice, "edit")
class MikrotikDeviceEditView(ObjectEditView):
    queryset = MikrotikDevice.objects.all()
    form = MikrotikDeviceForm


@register_model_view(MikrotikDevice, "delete")
class MikrotikDeviceDeleteView(ObjectDeleteView):
    queryset = MikrotikDevice.objects.all()


@register_model_view(MikrotikDevice, "bulk_import", detail=False)
class MikrotikDeviceBulkImportView(BulkImportView):
    queryset = MikrotikDevice.objects.all()
    # model_form = ViewImportForm # ToDo
    table = MikrotikDeviceTable


@register_model_view(MikrotikDevice, "bulk_edit", path="edit", detail=False)
class MikrotikDeviceBulkEditView(BulkEditView):
    queryset = MikrotikDevice.objects.all()
    # filterset = ViewFilterSet # ToDo
    table = MikrotikDeviceTable
    # form = ViewBulkEditForm # ToDo


@register_model_view(MikrotikDevice, "bulk_delete", path="delete", detail=False)
class MikrotikDeviceBulkDeleteView(BulkDeleteView):
    queryset = MikrotikDevice.objects.all()
    # filterset = ViewFilterSet # ToDo
    table = MikrotikDeviceTable
