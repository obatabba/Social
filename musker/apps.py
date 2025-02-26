from django.apps import AppConfig


class MuskerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'musker'

    def ready(self) -> None:
        from . import signals
        return super().ready()