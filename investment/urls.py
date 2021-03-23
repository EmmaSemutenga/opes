from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_investor/', views.add_investor, name='add_investor'),
    path('add_institution/', views.add_institution, name='add_institution'),
]