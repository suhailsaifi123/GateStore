from django.urls import path
from . import views

urlpatterns = [
    path('', views.gate_list, name='gate_list'),
    path('shop/', views.gate_list, name='shop'),
    path('preview/', views.live_preview, name='live_preview'),
    path('<slug:slug>/', views.gate_detail, name='gate_detail'),
    path('order/<slug:slug>/', views.place_order, name='place_order'),
] 