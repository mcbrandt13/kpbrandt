"""The router swagger application configuration."""
from django.apps import AppConfig


# pylint: disable=too-few-public-methods
class ArticleSwagger(AppConfig):
  """The application configuration."""
  name = 'articleswagger'

  def ready(self):
    """Initializes the data during app start up."""
    from django.conf import settings as django_settings
    from articleswagger import settings as swagger_settings

    super(ArticleSwagger, self).ready()

    # Update the Django global settings, if Swagger settings are missing.
    for setting_name in dir(swagger_settings):
      if setting_name.startswith('SWAGGER_'):
        if getattr(django_settings, setting_name, None) is None:
          val = getattr(swagger_settings, setting_name, None)
          setattr(django_settings, setting_name, val)
# pylint: enable=too-few-public-methods
