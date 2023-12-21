from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("query", views.query, name="query"),
    path("radical", views.radical, name="radical"),
    path("evolution", views.evolution, name="evolution"),
    path("visualization", views.visualization, name="visualization"),
]