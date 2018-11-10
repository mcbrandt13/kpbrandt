"""Router swagger URL patterns."""

from django.urls import path, re_path
from rest_framework_swagger import views
from articleswagger import settings


_SCHEMA_VIEW = views.get_swagger_view(title=settings.ROUTER_SWAGGER_TITLE)

# pylint: disable=invalid-name
urlpatterns = (
  re_path(r'^api$', _SCHEMA_VIEW, name='swagger'),
)
# pylint: enable=invalid-name
