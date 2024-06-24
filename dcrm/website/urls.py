from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register_user, name="register"),
    path('logout/', views.logout_user, name="logout"),
    path('record/<int:pk>', views.record, name="record"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('update/<int:pk>', views.update, name="update"),
    path('add/', views.add, name="add"),
]
