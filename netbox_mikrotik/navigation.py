from django.utils.translation import gettext_lazy as _
from netbox.plugins import PluginMenuButton, PluginMenuItem

from netbox.plugins import PluginMenu

configuration_item = PluginMenuItem(link="plugins:netbox_mikrotik:mikrotikdevice_list",
                                    link_text=_("Devices"),
                                    buttons=[PluginMenuButton("plugins:netbox_mikrotik:mikrotikdevice_add",
                                                              _("Add"),
                                                              "mdi mdi-plus-thick",
                                                              permissions=["netbox_mikrotik.add_device"]),
                                             PluginMenuButton("plugins:netbox_mikrotik:mikrotikdevice_bulk_import",
                                                              _("Import"),
                                                              "mdi mdi-upload",
                                                              permissions=["netbox_mikrotik.add_device"])])

menu = PluginMenu(label="Mikrotik",
                  groups=[(_("Configuration"), [configuration_item])],
                  icon_class="mdi mdi-router")
