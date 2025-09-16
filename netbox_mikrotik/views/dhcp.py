from netbox.views.generic import ObjectListView, ObjectView, ObjectEditView, ObjectDeleteView, BulkImportView, \
    BulkEditView, BulkDeleteView
from utilities.views import register_model_view

from netbox_mikrotik.models import MikrotikDhcpServer, MikrotikDhcpLease
from netbox_mikrotik.tables import MikrotikDhcpServerTable, MikrotikDhcpLeaseTable
from netbox_mikrotik.forms import MikrotikDhcpServerForm, MikrotikDhcpLeaseForm

__all__ = ("MikrotikDhcpServerListView",
           "MikrotikDhcpServerView",
           "MikrotikDhcpServerEditView",
           "MikrotikDhcpServerDeleteView",
           "MikrotikDhcpServerBulkImportView",
           "MikrotikDhcpServerBulkEditView",
           "MikrotikDhcpServerBulkDeleteView",
           "MikrotikDhcpLeaseListView",
           "MikrotikDhcpLeaseView",
           "MikrotikDhcpLeaseEditView",
           "MikrotikDhcpLeaseDeleteView",
           "MikrotikDhcpLeaseBulkImportView",
           "MikrotikDhcpLeaseBulkEditView",
           "MikrotikDhcpLeaseBulkDeleteView")


@register_model_view(MikrotikDhcpServer, "list", path="", detail=False)
class MikrotikDhcpServerListView(ObjectListView):
    queryset = MikrotikDhcpServer.objects.all()
    # filterset = filters.ConfiguredDhcpServerFilterSet ' ToDo
    # filterset_form = forms.ConfiguredDhcpServerForm ' ToDo
    table = MikrotikDhcpServerTable


@register_model_view(MikrotikDhcpServer)
class MikrotikDhcpServerView(ObjectView):
    queryset = MikrotikDhcpServer.objects.all()


@register_model_view(MikrotikDhcpServer, "add", detail=False)
@register_model_view(MikrotikDhcpServer, "edit")
class MikrotikDhcpServerEditView(ObjectEditView):
    queryset = MikrotikDhcpServer.objects.all()
    form = MikrotikDhcpServerForm


@register_model_view(MikrotikDhcpServer, "delete")
class MikrotikDhcpServerDeleteView(ObjectDeleteView):
    queryset = MikrotikDhcpServer.objects.all()


@register_model_view(MikrotikDhcpServer, "bulk_import", detail=False)
class MikrotikDhcpServerBulkImportView(BulkImportView):
    queryset = MikrotikDhcpServer.objects.all()
    # model_form = ViewImportForm # ToDo
    table = MikrotikDhcpServerTable


@register_model_view(MikrotikDhcpServer, "bulk_edit", path="edit", detail=False)
class MikrotikDhcpServerBulkEditView(BulkEditView):
    queryset = MikrotikDhcpServer.objects.all()
    # filterset = ViewFilterSet # ToDo
    table = MikrotikDhcpServerTable
    # form = ViewBulkEditForm # ToDo


@register_model_view(MikrotikDhcpServer, "bulk_delete", path="delete", detail=False)
class MikrotikDhcpServerBulkDeleteView(BulkDeleteView):
    queryset = MikrotikDhcpServer.objects.all()
    # filterset = ViewFilterSet # ToDo
    table = MikrotikDhcpServerTable


@register_model_view(MikrotikDhcpLease, "list", path="", detail=False)
class MikrotikDhcpLeaseListView(ObjectListView):
    queryset = MikrotikDhcpLease.objects.all()
    # filterset = filters.ConfiguredDhcpLeaseFilterSet ' ToDo
    # filterset_form = forms.ConfiguredDhcpLeaseForm ' ToDo
    table = MikrotikDhcpLeaseTable


@register_model_view(MikrotikDhcpLease)
class MikrotikDhcpLeaseView(ObjectView):
    queryset = MikrotikDhcpLease.objects.all()


@register_model_view(MikrotikDhcpLease, "add", detail=False)
@register_model_view(MikrotikDhcpLease, "edit")
class MikrotikDhcpLeaseEditView(ObjectEditView):
    queryset = MikrotikDhcpLease.objects.all()
    form = MikrotikDhcpLeaseForm


@register_model_view(MikrotikDhcpLease, "delete")
class MikrotikDhcpLeaseDeleteView(ObjectDeleteView):
    queryset = MikrotikDhcpLease.objects.all()


@register_model_view(MikrotikDhcpLease, "bulk_import", detail=False)
class MikrotikDhcpLeaseBulkImportView(BulkImportView):
    queryset = MikrotikDhcpLease.objects.all()
    # model_form = ViewImportForm # ToDo
    table = MikrotikDhcpLeaseTable


@register_model_view(MikrotikDhcpLease, "bulk_edit", path="edit", detail=False)
class MikrotikDhcpLeaseBulkEditView(BulkEditView):
    queryset = MikrotikDhcpLease.objects.all()
    # filterset = ViewFilterSet # ToDo
    table = MikrotikDhcpLeaseTable
    # form = ViewBulkEditForm # ToDo


@register_model_view(MikrotikDhcpLease, "bulk_delete", path="delete", detail=False)
class MikrotikDhcpLeaseBulkDeleteView(BulkDeleteView):
    queryset = MikrotikDhcpLease.objects.all()
    # filterset = ViewFilterSet # ToDo
    table = MikrotikDhcpLeaseTable