from django.apps import AppConfig


class DicasOportunidadesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dicas_oportunidades'
    verbose_name = 'Dicas Oportunidades'

    def ready(self):
        import dicas_oportunidades.signals
