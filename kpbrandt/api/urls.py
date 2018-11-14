from django.urls import path

from . import views
from .swagger_schema import SwaggerSchemaView

urlpatterns = [
               path('api', SwaggerSchemaView.as_view()),
               path('api/confucius', views.confucius, name='confucius'),
               path('api/bs', views.bs, name='bs'),
               path('api/bart', views.bart, name='bart'),
               path('api/weather', views.weather, name='weather')
               ]
