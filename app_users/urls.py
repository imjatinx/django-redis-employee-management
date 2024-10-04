from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cached/', views.cached, name="cached"),
]
