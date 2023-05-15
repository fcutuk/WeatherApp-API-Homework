from django.urls import path

from . import views

urlpatterns = [
    path("/", views.index, name="index"),
    path('weather-current', views.current_weather),
    path('weather-forecast', views.forcast_weather),
    path('weather-history', views.history_weather),
]