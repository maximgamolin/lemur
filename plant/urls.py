from django.urls import path

from plant import views

urlpatterns = [
    path('workpiece/<int:pk>/', views.WorkpieceDetailView.as_view()),
    path('init-workpiece/', views.InitWorkpieceView.as_view()),
    path('create-data-peace/', views.CreateDataSampleView.as_view()),
    path('move-datasets-to-data-sample/', views.MoveDatasetToDataSampleView.as_view()),
    path('add-joins/', views.AddWorkpieceJoinsView.as_view()),
    path('add-features/', views.AddWorkpieceFeatures.as_view()),
    path('add-limits/', views.AddLimitsView.as_view()),
    path('create-task-text/', views.CreateTaskTextView.as_view()),
    path('set-workpice-pricing/', views.SetWorkpiecePricingView.as_view()),
    path('calculite-workpice-dataset-prices/', views.CalculateResultDatasetPrelimPriceView.as_view())
]