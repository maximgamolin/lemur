from django.urls import path, re_path

from core import views

urlpatterns = [
    path('me/', views.MeView.as_view()),
    path('schema-block/', views.SchemaBlockView.as_view()),


]
