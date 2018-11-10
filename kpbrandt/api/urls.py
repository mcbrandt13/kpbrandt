from django.urls import path, re_path

from . import views


urlpatterns = [re_path(r'api$', views.schema_view),
               path('api/confucius', views.confucius, name='confucius'),
               path('api/bs', views.bs, name='bs'),
               path('api/bart', views.bart, name='bart')
               ]