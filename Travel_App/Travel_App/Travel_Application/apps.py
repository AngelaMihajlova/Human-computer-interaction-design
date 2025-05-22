from django.apps import AppConfig


class TravelApplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Travel_Application'

    def ready(self):
        from . import signals