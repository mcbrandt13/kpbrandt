"""Custom template tags to support swagger pages."""

from django import template

from articleswagger import settings


register = template.Library()  # pylint: disable=invalid-name


@register.simple_tag
def get_swagger_setting(key):
  """Gets the swagger setting.

  Gets the value for the specified key name.

  Args:
    key: The setting key name.

  Returns:
    The value of the router swagger setting, if the key exists. Else, None.
  """
  return settings.SWAGGER_SETTINGS.get(key)
