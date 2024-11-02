from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('manager_customer/', views.manager_customer, name='manager_customer'),
    path('manager_scheduling/', views.manager_scheduling, name='manager_scheduling'),
    path('manager_service/', views.manager_service, name='manager_service'),
    path('manager_type_service/', views.manager_type_service, name='manager_type_service'),
    path('manager_type_vehicle/', views.manager_type_vehicle, name='manager_type_vehicle'),

    path('register_customer/', views.register_customer, name='register_customer'),
    path('register_scheduling/', views.register_scheduling, name='register_scheduling'),
    path('register_service/', views.register_service, name='register_service'),
    path('register_type_service/', views.register_type_service, name='register_type_service'),
    path('register_type_vehicle/', views.register_type_vehicle, name='register_type_vehicle'),

    # rotas para chamar por um botão nos managers
    path('edit_customer/', views.edit_customer, name='edit_customer'),
    path('edit_scheduling/', views.edit_scheduling, name='edit_scheduling'),
    path('edit_service/', views.edit_service, name='edit_service'),
    path('edit_type_service/', views.edit_type_service, name='edit_type_service'),
    path('edit_type_vehicle/', views.edit_type_vehicle, name='edit_type_vehicle'),

    path('bi_report/', views.bi_report, name='bi_report'),
    path('bi_analysis/', views.bi_analysis, name='bi_analysis'),

    path('site_edit/', views.site_edit, name='site_edit'),
]