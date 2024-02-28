from django.contrib import admin
from django.apps import apps
# from

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

admin.site.site_header = "Sakhib Admin panel"
admin.site.index_title = "Admin settings"
