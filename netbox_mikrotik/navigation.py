from django.utils.translation import gettext_lazy as _
from netbox.plugins import PluginMenuButton, PluginMenuItem

from netbox.plugins import PluginMenu

menu = PluginMenu(label="Mikrotik",
                  groups=[(_("Configuration"), [
                      PluginMenuItem(link="plugins:netbox_mikrotik:mikrotikdevice_list",
                                     link_text=_("Devices"),
                                     buttons=[PluginMenuButton("plugins:netbox_mikrotik:mikrotikdevice_add",
                                                               _("Add"),
                                                               "mdi mdi-plus-thick",
                                                               permissions=["netbox_mikrotik.add_device"]),
                                              PluginMenuButton("plugins:netbox_mikrotik:mikrotikdevice_bulk_import",
                                                               _("Import"),
                                                               "mdi mdi-upload",
                                                               permissions=["netbox_mikrotik.add_device"])])
                  ]),
                          (_("DHCP"), [
                              PluginMenuItem(link="plugins:netbox_mikrotik:mikrotikdhcpserver_list",
                                             link_text=_("Servers"),
                                             buttons=[PluginMenuButton("plugins:netbox_mikrotik:mikrotikdhcpserver_add",
                                                                       _("Add"),
                                                                       "mdi mdi-plus-thick",
                                                                       permissions=["netbox_mikrotik.add_dhcpserver"]),
                                                      PluginMenuButton(
                                                          "plugins:netbox_mikrotik:mikrotikdhcpserver_bulk_import",
                                                          _("Import"),
                                                          "mdi mdi-upload",
                                                          permissions=["netbox_mikrotik.add_dhcpserver"])]),
                              PluginMenuItem(link="plugins:netbox_mikrotik:mikrotikdhcplease_list",
                                             link_text=_("Leases"),
                                             buttons=[PluginMenuButton("plugins:netbox_mikrotik:mikrotikdhcplease_add",
                                                                       _("Add"),
                                                                       "mdi mdi-plus-thick",
                                                                       permissions=["netbox_mikrotik.add_dhcplease"]),
                                                      PluginMenuButton(
                                                          "plugins:netbox_mikrotik:mikrotikdhcplease_bulk_import",
                                                          _("Import"),
                                                          "mdi mdi-upload",
                                                          permissions=["netbox_mikrotik.add_dhcplease"])])
                          ])],
                  icon_class="mdi mdi-router")
