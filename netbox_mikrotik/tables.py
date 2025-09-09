from django_tables2 import Column
from django.utils.translation import gettext_lazy as _
from netbox.tables import NetBoxTable, ToggleColumn, ActionsColumn

from netbox_mikrotik.models import MikrotikDevice


class MikrotikDeviceTable(NetBoxTable):
    pk = ToggleColumn()
    # noinspection PyTypeChecker
    name = Column(accessor="str",
                  linkify=True,
                  verbose_name=_("Name"))
    # noinspection PyTypeChecker
    ip_address = Column(accessor="ip_address",
                        linkify=True,
                        verbose_name=_("IP Address"))

    actions = ActionsColumn(actions=())

    class Meta(NetBoxTable.Meta):
        model = MikrotikDevice
        fields = (
            "pk",
            "name",
            "ip_address",
            "actions"
        )
        default_columns = (
            "name",
            "ip_address"
            "actions",
        )
