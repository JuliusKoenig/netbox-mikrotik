from importlib.metadata import metadata
from netbox.plugins import PluginConfig

meta = metadata(__name__)

package_version = meta.get("Version").split(".")
version = ".".join(package_version[:3])
release_track = ""
if len(package_version) == 4:
    if package_version[3].startswith("dev"):
        release_track = "dev"
    elif package_version[3].startswith("b"):
        release_track = "beta"


class NetBoxMikrotikConfig(PluginConfig):
    name = __name__
    verbose_name = "NetBox Mikrotik"
    description = meta.get("description")
    version = version
    release_track = release_track
    base_url = "netbox-mikrotik"
    min_version = "4.3.0"
    author = meta.get("author")
    author_email = meta.get("author_email")


config = NetBoxMikrotikConfig
