from django.urls import path
from . import views

app_name="encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/random", views.random_entry, name="random"),
    path("wiki/<str:title>", views.pages, name="pages"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("wiki/<str:title>/edit", views.edit, name="edit")
]
    
