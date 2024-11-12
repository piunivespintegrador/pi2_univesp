from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('health/', views.health, name='health'),

    path('public_register_service/', views.public_register_service, name='public_register_service'),
]