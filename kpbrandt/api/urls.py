from django.urls import path, re_path
from rest_framework_swagger.views import get_swagger_view

from . import views



#schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [#re_path(r'api$', views.schema_view),
               path('api/confucius', views.confucius, name='confucius'),
               path('api/bs', views.bs, name='bs'),
               path('api/bart', views.bart, name='bart')
               ]