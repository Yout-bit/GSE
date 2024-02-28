from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_view, name="home"),
    path("scanner", views.scanner_view, name="scanner")
]