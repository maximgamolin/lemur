from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('me/', views.MeView.as_view())
]