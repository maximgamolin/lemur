from django.urls import path

from stock import views

urlpatterns = [
    path('datasets/', views.DatasetListView.as_view()),
    path('datasets-search/', views.DatasetSearchView.as_view()),
]