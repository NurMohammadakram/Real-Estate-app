from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.profile, name='profile'),
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('change_password/', views.change_password, name='change_password'),
]