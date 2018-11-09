from django.urls import path


from . import views

urlpatterns = [path('confucius', views.confucius, name='confucius'),
               path('bs', views.bs, name='bs'),
               path('bart', views.bart, name='bart')
               ]