from django.apps import apps
from django.contrib import admin


for model in apps.get_app_config("demo").get_models():
    admin.site.register(model)
