from django.apps import AppConfig
# added a new line


class App1Config(AppConfig):
    """configuration for board app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app1'
