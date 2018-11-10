"""Unit tests for Swagger."""
import json

from django import test
from django import urls

from articleswagger import settings

_SWAGGER_VIEW_NAME = "swagger"

_SWAGGER_URL = '/api'


class RouterSwaggerTest(test.TestCase):
  """Test cases for Swagger."""

  def test_resolve_view_name_should_succeed(self):
    """Test resolving the swagger view name."""
    actual_url = urls.reverse(_SWAGGER_VIEW_NAME)
    self.assertEqual(actual_url, _SWAGGER_URL)

  def test_resolve_url_should_succeed(self):
    """Test resolving the swagger URL."""
    resolver = urls.resolve(_SWAGGER_URL)
    self.assertIsNotNone(resolver)
    self.assertEqual(resolver.view_name, _SWAGGER_VIEW_NAME)

  def test_swagger_page_should_succeed(self):
    """Test the swagger landing page should succeed."""
    response = self.client.get(urls.reverse(_SWAGGER_VIEW_NAME))
    self.assertIsNotNone(response)
    self.assertEqual(response.status_code, 200)
    content = json.loads(response.content.decode("utf-8"))
    actual_meta = content.get('_meta')
    self.assertIn('title', actual_meta)
    self.assertEqual(actual_meta.get('title'), settings.ROUTER_SWAGGER_TITLE)
