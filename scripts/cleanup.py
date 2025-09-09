from django.contrib.contenttypes.models import ContentType

# Replace 'pluginname' with your plugin's actual name
stale_types = ContentType.objects.filter(app_label="netbox_mikrotik")
for ct in stale_types:
    print(ct)

from django.contrib.auth.models import Permission
for ct in stale_types:
    perms = Permission.objects.filter(content_type=ct)
    print(list(perms))

for ct in stale_types:
    Permission.objects.filter(content_type=ct).delete()

stale_types.delete()
exit()

