from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('sale/', views.for_sale, name='for_sale'),
    path('rent/', views.rent, name='rent'),
    path('properties/', views.properties, name='properties'),
    path('owners/', views.owners, name='owners'),
]