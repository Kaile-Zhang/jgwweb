from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.Search, name="Search"),
    path("evolution/", views.evolution, name="evolution"),
]
