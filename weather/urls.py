from django.urls import path
from . import views

urlpatterns = [
    path('api/weather/', views.get_weather, name='get_weather'),
    path('', views.weather_page, name='weather_page'),
]
