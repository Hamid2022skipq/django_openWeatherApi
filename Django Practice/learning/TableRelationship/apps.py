from django.apps import AppConfig
class TablerelationshipConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TableRelationship'
    def ready(self):
        import TableRelationship.signals
