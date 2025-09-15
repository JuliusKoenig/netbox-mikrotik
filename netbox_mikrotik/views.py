from netbox.views.generic import ObjectListView, ObjectView, ObjectEditView, ObjectDeleteView, BulkImportView, \
    BulkEditView, BulkDeleteView
from utilities.views import register_model_view

from netbox_mikrotik.models import MikrotikDevice, SyncGroup
from netbox_mikrotik.tables import MikrotikDeviceTable, SyncGroupTable
from netbox_mikrotik.forms import MikrotikDeviceForm, SyncGroupForm


# --- MikrotikDevice Views ---------------------------------------------------------------------------------------------

@register_model_view(MikrotikDevice, "list", path="", detail=False)
class MikrotikDeviceListView(ObjectListView):
    queryset = MikrotikDevice.objects.all()
    # filterset = filters.ConfiguredDeviceFilterSet ' ToDo
    # filterset_form = forms.ConfiguredDeviceForm ' ToDo
    table = MikrotikDeviceTable


@register_model_view(MikrotikDevice)
class MikrotikDeviceView(ObjectView):
    queryset = MikrotikDevice.objects.all()


@register_model_view(MikrotikDevice, "add", detail=False)
@register_model_view(MikrotikDevice, "edit")
class MikrotikEditView(ObjectEditView):
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


# --- SyncGroup Views --------------------------------------------------------------------------------------------------

@register_model_view(SyncGroup, "list", path="", detail=False)
class SyncGroupListView(ObjectListView):
    queryset = SyncGroup.objects.all()
    # filterset = filters.ConfiguredDeviceFilterSet ' ToDo
    # filterset_form = forms.ConfiguredDeviceForm ' ToDo
    table = SyncGroupTable


@register_model_view(SyncGroup)
class SyncGroupView(ObjectView):
    queryset = SyncGroup.objects.all()


@register_model_view(SyncGroup, "add", detail=False)
@register_model_view(SyncGroup, "edit")
class MikrotikEditView(ObjectEditView):
    queryset = SyncGroup.objects.all()
    form = SyncGroupForm


@register_model_view(SyncGroup, "delete")
class SyncGroupDeleteView(ObjectDeleteView):
    queryset = SyncGroup.objects.all()


@register_model_view(SyncGroup, "bulk_import", detail=False)
class SyncGroupBulkImportView(BulkImportView):
    queryset = SyncGroup.objects.all()
    # model_form = ViewImportForm # ToDo
    table = SyncGroupTable


@register_model_view(SyncGroup, "bulk_edit", path="edit", detail=False)
class SyncGroupBulkEditView(BulkEditView):
    queryset = SyncGroup.objects.all()
    # filterset = ViewFilterSet # ToDo
    table = SyncGroupTable
    # form = ViewBulkEditForm # ToDo


@register_model_view(SyncGroup, "bulk_delete", path="delete", detail=False)
class SyncGroupBulkDeleteView(BulkDeleteView):
    queryset = SyncGroup.objects.all()
    # filterset = ViewFilterSet # ToDo
    table = SyncGroupTable
