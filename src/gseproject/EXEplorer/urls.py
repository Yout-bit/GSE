from django.urls import path
from . import views
from .views import reset_user_profile


urlpatterns = [
    path("", views.home_view, name="home"),
    path('health', views.health, name='health'),
    path('game/', views.game_view, name='game'),
    path('scanner/', views.scanner_view, name= 'scanner'),
    path('handle-scanned-number/', views.handle_scanned_number, name='handle_scanned_number'),
    path('shop/', views.shop_view, name='shop'),
    path('tree/', views.tree_view, name='tree'),
    path('reset_user_profile', reset_user_profile, name='reset_user_profile'),
    path('api/get_cherries_value/', views.get_cherries_value, name='get_cherries_value'),
    path('api/update_cherries_value/', views.update_cherries_value, name='update_cherries_value'),
    path('api/get_carbon_footprint_value/', views.get_carbon_footprint_value, name='get_carbon_footprint_value'),
    path('api/increment_carbon_footprint/', views.increment_carbon_footprint, name='increment_carbon_footprint'),
    path('api/decrement_carbon_footprint/', views.decrement_carbon_footprint, name='decrement_carbon_footprint'),
    path('start-pet-walk/', views.petDisappear, name='start-pet-walk'),
    path('pet-check', views.petCheck, name = 'pet-check'),
    path('scan/', views.scan_view, name='scan'),
]
