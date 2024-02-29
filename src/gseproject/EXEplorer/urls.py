from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path('game', views.game_view, name='game'),
]