from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('videos$', views.videos, name='videos'),
    path('videos/ava', views.ava, name='ava')
]
