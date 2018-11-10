from django.urls import path


from . import views

urlpatterns = [path('api/confucius', views.confucius, name='confucius'),
               path('api/bs', views.bs, name='bs'),
               path('api/bart', views.bart, name='bart')
               ]