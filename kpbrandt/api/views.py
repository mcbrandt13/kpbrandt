import random
import sys

from bs4 import BeautifulSoup
import coreapi
import coreschema
from django.conf import settings
import requests
from rest_framework.decorators import api_view, renderer_classes, parser_classes, schema
from rest_framework import schemas, status, generics, mixins
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser

from .serializers import ApiWeatherSerializer
from .serializers import SimpleMsgSerializer
from .serializers import GenericSerializer
from .serializers import ApiWeatherResponseSerializer
from .serializers import QuotesSerializer
from . import models


@api_view(['GET'])
@schema(schemas.ManualSchema(fields=[coreapi.Field('city', required=True,
                                                   location='query',
                                                   schema=coreschema.String(),
                                                   description='City'),
                                     coreapi.Field('state', required=True,
                                                   location='query',
                                                   schema=coreschema.String(),
                                                   description='State')
                                     ]))
@parser_classes((JSONParser,))
@permission_classes((AllowAny,))
@renderer_classes((JSONRenderer,))
def weather(request):
    """
    Get the forecast by providing city and state.
    """
    serializer = ApiWeatherSerializer(data=request.query_params)
    serializer.is_valid(raise_exception=True)
    key = settings.WEATHER_API_KEY
    city = request.query_params.get('city').strip().title()
    state = request.query_params.get('state').strip().upper()
    base_url = 'http://api.wunderground.com/api/'
    url = '{0}/{1}/geolookup/conditions/forecast/q/{2}/{3}.json'.format(base_url,
                                                                        key,
                                                                        state,
                                                                        city.replace(' ', '_'))
    r = requests.get(url)
    if not r.ok or r.json().get('response').get('error'):
        msg = r.json().get('response').get('error').get('description')
        response_serializer = GenericSerializer({'city': [msg]}, field='city')
        return Response(response_serializer.data,
                        status=status.HTTP_400_BAD_REQUEST)
    forecast = {}
    for day in r.json().get('forecast').get('txt_forecast').get('forecastday'):
        if 'night' not in day['title'].lower():
            forecast[day.get('title')] = day.get('fcttext')
    response_serializer = ApiWeatherResponseSerializer(
      {
        'Location': ', '.join([city, state]),
        'Conditions': r.json().get('current_observation').get('weather'),
        'Temperature': r.json().get('current_observation').get('feelslike_f'),
        'Forecast': forecast
      }
    )
    return Response(response_serializer.data)


@api_view(['GET'])
@permission_classes((AllowAny,))
@renderer_classes((JSONRenderer,))
def bart(request):
    """Query BART API for delays in service"""
    url = 'http://api.bart.gov/api/bsa.aspx?cmd=bsa&key={0}' \
          '&date=today'.format(settings.BART_KEY)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    msg = ''
    if soup.bsa.station.text:
        msg = '{0}: '.format(soup.bsa.station.text)
    msg += soup.bsa.description.text
    serialized = SimpleMsgSerializer({'msg': msg})
    return Response(serialized.data)


@api_view(['GET'])
@permission_classes((AllowAny,))
@renderer_classes((JSONRenderer,))
def confucius(request):
    """Random Confucius quote"""
    msg = random.choice(settings.CONFUCIUS_QUOTES)
    serialized = SimpleMsgSerializer({'msg': msg})
    return Response(serialized.data)


@api_view(['GET'])
@permission_classes((AllowAny,))
@renderer_classes((JSONRenderer,))
def bs(request):
    """Generate some corporate bs"""
    start = ['You should', 'We need to', "Let's"]
    phrase = ' '.join([random.choice(start),
                       str(models.Adverb.objects.random()),
                       str(models.Verb.objects.random()),
                       str(models.Adjective.objects.random()),
                       str(models.Noun.objects.random())])
    serialized = SimpleMsgSerializer({'msg': '{0}.'.format(phrase)})
    return Response(serialized.data)


class BaseQuotes(generics.GenericAPIView):
    """Base class for Quotes views setting up classes"""
    queryset = models.Quotes.objects.all()
    serializer_class = QuotesSerializer
    renderer_classes = (JSONRenderer,)
    permission_classes = (AllowAny,)
    throttle_scope = 'quotes'


class QuotesList(BaseQuotes, mixins.ListModelMixin, mixins.CreateModelMixin):
    """Basic class based view example."""

    def get(self, request, *args, **kwargs):
        """Return all quotes, paginated"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Create a new quote."""
        return self.create(request, *args, **kwargs)


class QuotesDetail(BaseQuotes, mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """Detailed view of quote."""

    def get(self, request, *args, **kwargs):
        """Returns a specific quote."""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Updates a specific quote."""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Delete a quote."""
        return self.destroy(request, *args, **kwargs)


@permission_classes((AllowAny,))
@renderer_classes((JSONRenderer,))
def error_page(request):
    type_, value, traceback = sys.exc_info()
    return Response({'message': str(value)}, status=500)
