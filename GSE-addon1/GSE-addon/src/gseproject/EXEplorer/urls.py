from django.urls import path
from . import views
from .views import coin_view

urlpatterns = [
    path("", views.home_view, name="home"),
    path('coin/', coin_view, name='coin-view'),

]