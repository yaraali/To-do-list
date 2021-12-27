from django.urls import path
from . import views

urlpatterns = [
	path('', views.Home, name="home"),
	path('updateTask/<str:pk>/', views.updateTask, name="updateTask"),
	path('deleteTask/<str:pk>/', views.deleteTask, name="deleteTask"),
]