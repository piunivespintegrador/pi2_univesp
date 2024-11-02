from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('customer/manager_customer/', views.manager_customer, name='manager_customer'),
    path('customer/register_customer/', views.register_customer, name='register_customer'),
    path('customer/edit_customer/', views.edit_customer, name='edit_customer'),
    path('customer/delete_customer/', views.delete_customer, name='delete_customer'),

    path('scheduling/manager_scheduling/', views.manager_scheduling, name='manager_scheduling'),
    path('scheduling/register_scheduling/', views.register_scheduling, name='register_scheduling'),
    path('scheduling/edit_scheduling/', views.edit_scheduling, name='edit_scheduling'),

    path('service/manager_service/', views.manager_service, name='manager_service'),
    path('service/register_service/', views.register_service, name='register_service'),
    path('service/edit_service/', views.edit_service, name='edit_service'),

    path('type_service/manager_type_service/', views.manager_type_service, name='manager_type_service'),
    path('type_service/register_type_service/', views.register_type_service, name='register_type_service'),
    path('type_service/edit_type_service/', views.edit_type_service, name='edit_type_service'),

    path('type_vehicle/manager_type_vehicle/', views.manager_type_vehicle, name='manager_type_vehicle'),
    path('type_vehicle/register_type_vehicle/', views.register_type_vehicle, name='register_type_vehicle'),
    path('type_vehicle/edit_type_vehicle/', views.edit_type_vehicle, name='edit_type_vehicle'),

    path('business_intelligence/bi_report/', views.bi_report, name='bi_report'),
    path('business_intelligence/bi_analysis/', views.bi_analysis, name='bi_analysis'),

    path('site/site_edit/', views.site_edit, name='site_edit'),
]