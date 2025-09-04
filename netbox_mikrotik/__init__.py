from netbox.plugins import PluginConfig

__title__ = "netbox-mikrotik"
__description__ = "Sync IP-Addresses to Mikrotik Address Lists and more."
__version__ = "0.1.0.dev1"
__author__ = "Julius Koenig"
__author_email__ = "info@bastelquartier.de"
__license__ = "GPL-3.0"
__license_url__ = "https://www.gnu.org/licenses/gpl-3.0.md"
__terms_of_service__ = "https://bastelquartier.de/terms-of-service"


class NetBoxMikrotikConfig(PluginConfig):
    name = __title__
    verbose_name = "NetBox Mikrotik"
    description = __description__
    release_track = "dev"
    version = __version__
    base_url = "netbox-mikrotik"
    min_version = "4.3.0"
    author = __author__
    author_email = __author_email__

config = NetBoxMikrotikConfig
