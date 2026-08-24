from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('acerca-de-mi/', views.about, name='about_me'),
]