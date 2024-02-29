from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path('health', views.health, name='health'),
    path('game', views.game_view, name='game'),
    path('scanner', views.scanner_view, name= 'scanner'),
]