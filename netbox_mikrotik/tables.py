from django_tables2 import Column, BooleanColumn, DateTimeColumn, LinkColumn
from django.utils.translation import gettext_lazy as _
from netbox.tables import NetBoxTable, ToggleColumn, ActionsColumn

from netbox_mikrotik.models import MikrotikDevice


class MikrotikDeviceTable(NetBoxTable):
    pk = ToggleColumn()
    # noinspection PyTypeChecker
    name = Column(linkify=True,
                  verbose_name=_("Name"))
    # noinspection PyTypeChecker
    ip_address = Column(linkify=True,
                        verbose_name=_("IP Address"))
    address_list_sync = BooleanColumn(verbose_name=_("Address List Synchronization"))
    dns_sync = BooleanColumn(verbose_name=_("DNS Synchronization"))
    dhcp_sync = BooleanColumn(verbose_name=_("DHCP Synchronization"))
    last_run = DateTimeColumn(verbose_name=_("Last Run"))

    class Meta(NetBoxTable.Meta):
        model = MikrotikDevice
        fields = (
            "pk",
            "name",
            "ip_address",
            "address_list_sync",
            "dns_sync",
            "dhcp_sync",
            "last_run",
            "actions"
        )
        default_columns = (
            "name",
            "ip_address",
            "address_list_sync",
            "dns_sync",
            "dhcp_sync",
            "last_run",
            "actions"
        )
