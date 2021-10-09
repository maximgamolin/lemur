from django.urls import path

from plant import views

urlpatterns = [
    path('workpiece/<int:pk>/', views.WorkpieceDetailView.as_view()),
    path('init-workpiece/', views.InitWorkpieceView.as_view()),
    path('create-data-peace/', views.CreateDataSampleView.as_view())
]