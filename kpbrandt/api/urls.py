from django.urls import path

from . import views

urlpatterns = [
               path('api/confucius', views.confucius, name='confucius'),
               path('api/bs', views.bs, name='bs'),
               path('api/bart', views.bart, name='bart'),
               path('api/weather', views.weather, name='weather'),
               path('api/quotes', views.QuotesList.as_view()),
               path('api/quotes/<int:pk>', views.QuotesDetail.as_view()),
               path('api/quotes/random', views.QuotesRandom.as_view()),
               path('api/reversed', views.reverse_string, name='reversed')
               ]
