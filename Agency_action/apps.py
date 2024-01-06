from django.apps import AppConfig
from django.contrib.admin.apps import *

class AgencyConfig(AdminConfig):
    default_site='Agency_action.admin.ModelAdmin'







class AgencyActionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Agency_action'
    class Meta:
        verbose_name='Linkin agency333'
