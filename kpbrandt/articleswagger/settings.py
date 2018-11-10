"""Swagger specific settings."""

API_VERSION = '1.0'

ROUTER_SWAGGER_TITLE = 'API v%s' % API_VERSION

SWAGGER_SETTINGS = {
  'EXCLUDE_URL_NAMES': [],
  'EXCLUDE_NAMESPACES': [],
  'API_VERSION': API_VERSION,
  'API_PATH': '/api',
  'RELATIVE_PATHS': False,
  'SUPPORTED_SUBMIT_METHODS': (
    'get',
    'post',
    'put',
    'patch',
    'delete'),
  'APIS_SORTER': None,
  'API_KEY': '',
  'IS_AUTHENTICATED': False,
  'IS_SUPERUSER': False,
  'UNAUTHENTICATED_USER': 'django.contrib.auth.models.AnonymousUser',
  'PERMISSION_DENIED_HANDLER': None,
  'RESOURCE_ACCESS_HANDLER': None,
  'DOC_EXPANSION': 'none',
  'JSON_EDITOR': False,
  'VALIDATOR_URL': None,
}
