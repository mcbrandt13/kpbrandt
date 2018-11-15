from django.urls import path

from . import views
from rest_framework.documentation import include_docs_urls

urlpatterns = [
               path('api/confucius', views.confucius, name='confucius'),
               path('api/bs', views.bs, name='bs'),
               path('api/bart', views.bart, name='bart'),
               path('api/weather', views.weather, name='weather')
               ]
