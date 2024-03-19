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
    path('tree/', views.tree_view, name='tree'),
    path('reset/', views.reset_user_profile, name='reset'),
    path('api/get_cherries_value/', views.get_cherries_value, name='get_cherries_value'),
    path('api/get_carbon_footprint_value/', views.get_carbon_footprint_value, name='get_carbon_footprint_value'),
]