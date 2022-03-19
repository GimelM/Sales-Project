from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name="home"),
    path('EmpleadosListView', EmpleadosListView.as_view(), name='EmpleadosListView'),
    path('EmpleadosCreateView', EmpleadosCreateView.as_view(), name='EmpleadosCreateView'),
    path('EmpleadoUpdate/<int:pk>', EmpleadosUpdateView.as_view(), name='EmpleadoUpdate'),
    path('EmpleadoDelete/<int:pk>', EmpleadosDeleteView.as_view(), name='EmpleadoDelete'),
    path('EmpleadoDetailView/<int:pk>', EmpleadosDetailView.as_view(), name='EmpleadoDetail'),
]