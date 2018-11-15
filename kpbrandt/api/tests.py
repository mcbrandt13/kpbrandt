from unittest import mock

from django.test import TestCase, Client
from django.conf import settings

from . import models


#TODO Mock a weather api response
_MOCKED_API_WEATHER_RESPONSE_DATA = {
    "response": {
        "version": "0.1",
        "termsofService": "http://www.wunderground.com/weather/api/d/terms.html",
        "features": {
            "geolookup": 1
            ,
            "conditions": 1
            ,
            "forecast": 1
        }
        ,
        "error": {
            "type": "querynotfound"
            , "description": "No cities match your search query"
        }
    }
}

class _FakeResponse(object):
    """Fake HTTP response."""

    def __init__(self, status_code=200, ok=True, text=None, data=None):
        self.status_code = status_code
        self.ok = ok
        self.text = text
        self._data = data or {}

    def raise_for_status(self):
        pass

    def json(self):
        """
        :return: The request data.
        """
        return self._data

    def __str__(self, *unused_args, **unused_kwargs):
        return '''{
        'ok': %s,
        'status_code': %s,
        'data': %s'
        }''' % (self.ok, self.status_code, self._data)

class TestApi(TestCase):
    """Test the various api app endpoints"""
    def setUp(self):
        self.client = Client()

        models.Adverb(word='test').save()
        models.Adjective(word='test').save()
        models.Noun(word='test').save()
        models.Verb(word='test').save()

    def test_confucius(self):
        """Test /confucius returns value from list"""
        response = self.client.get('/api/confucius')
        self.assertIn(response.json().get('msg'), settings.CONFUCIUS_QUOTES)

    def test_bs(self):
        """Test /bs returns string compiled from models"""
        response = self.client.get('/api/bs')
        self.assertEqual(response.status_code, 200)

    def test_weather_pass(self):
        data = {'state': 'CA',
                'city': 'Redding'}
        response = self.client.get('/api/weather', data=data)
        self.assertEqual(response.status_code, 200)

    def test_weather_state_fails(self):
        data = {'state': 'CB',
                'city': 'Redding'}

        response = self.client.get('/api/weather', data=data)
        self.assertEqual(response.status_code, 400)

    @mock.patch('requests.get', autospec=True,
                side_effect=[_FakeResponse(data=_MOCKED_API_WEATHER_RESPONSE_DATA)])
    def test_weather_city_fails(self, mock_request):
        data={'state': 'CA',
              'city': 'fakecity'
              }
        response = self.client.get('/api/weather', data=data)
        self.assertEqual(mock_request.call_count, 1)
        expected = _MOCKED_API_WEATHER_RESPONSE_DATA.get('response').get('error').get('description')
        self.assertEqual(response.json().get('city'), [expected])


