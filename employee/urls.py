from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'employee-home'),
    path('add/', views.add_employee, name='add-employee'),
    path('update_employee/<int:pk>/', views.update_employee, name='update-employee'),
    path('detail/<int:pk>/', views.detail_employee, name='detail-employee'),
]