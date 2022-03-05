from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('search', views.new_search, name='search'),
    path('mic', views.mic, name='mic'),
    path('speak', views.speak, name='speak'),
    path('speaker', views.speaker, name='speaker')
]
