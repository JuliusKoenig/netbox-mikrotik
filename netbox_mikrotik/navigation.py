from django.utils.translation import gettext_lazy as _
from netbox.plugins import PluginMenuButton, PluginMenuItem

from netbox.plugins import PluginMenu

mikrotik_device_item = PluginMenuItem(link="plugins:netbox_mikrotik:mikrotikdevice_list",
                                      link_text=_("Devices"),
                                      buttons=[PluginMenuButton("plugins:netbox_mikrotik:mikrotikdevice_add",
                                                                _("Add"),
                                                                "mdi mdi-plus-thick",
                                                                permissions=["netbox_mikrotik.add_device"]),
                                               PluginMenuButton("plugins:netbox_mikrotik:mikrotikdevice_bulk_import",
                                                                _("Import"),
                                                                "mdi mdi-upload",
                                                                permissions=["netbox_mikrotik.add_device"])])

sync_group_item = PluginMenuItem(link="plugins:netbox_mikrotik:syncgroup_list",
                                 link_text=_("Synchronisation Groups"),
                                 buttons=[PluginMenuButton("plugins:netbox_mikrotik:syncgroup_add",
                                                           _("Add"),
                                                           "mdi mdi-plus-thick",
                                                           permissions=["netbox_mikrotik.add_syncgroup"]),
                                          PluginMenuButton("plugins:netbox_mikrotik:syncgroup_bulk_import",
                                                           _("Import"),
                                                           "mdi mdi-upload",
                                                           permissions=["netbox_mikrotik.add_syncgroup"])])

menu = PluginMenu(label="Mikrotik",
                  groups=[(_("Configuration"), [mikrotik_device_item, sync_group_item])],
                  icon_class="mdi mdi-router")
