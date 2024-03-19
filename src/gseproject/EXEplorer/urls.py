from django.urls import path
from . import views
from .views import handle_scanned_number

urlpatterns = [
    path("", views.home_view, name="home"),
    path('health', views.health, name='health'),
    path('game', views.game_view, name='game'),
    path('scanner', views.scanner_view, name= 'scanner'),
    path('handle-scanned-number/', handle_scanned_number, name='handle_scanned_number'),
    path('shop/', views.shop_view, name='shop'),
    path('tree/', views.tree_view, name='tree')
]