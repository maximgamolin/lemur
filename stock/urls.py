from django.contrib import admin
from django.urls import path, include
from stock import views

urlpatterns = [
    path('datasets/', views.DatasetListView.as_view())
]