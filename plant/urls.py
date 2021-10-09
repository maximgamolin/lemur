from django.urls import path

from plant import views

urlpatterns = [
    path('init-workpiece/', views.InitWorkpieceView.as_view())
]