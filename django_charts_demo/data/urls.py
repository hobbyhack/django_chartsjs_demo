from django.urls import path
from data import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard')
]