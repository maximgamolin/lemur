from django.urls import path
from market import views
from django.urls import path

from market import views

urlpatterns = [
    path('collection-items/', views.CollectionItemView.as_view())
]