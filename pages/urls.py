from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('warranty/', views.warranty, name='warranty'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('installation/', views.installation, name='installation'),
] 