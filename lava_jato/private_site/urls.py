from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('manage_scheduling/', views.manage_scheduling, name='manage_scheduling'),
    path('make_scheduling/', views.make_scheduling, name='make_scheduling'),
    path('report/', views.report, name='report'),
    path('site_edit/', views.site_edit, name='site_edit'),
]