from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
    path("", views.index, name="index"),
    path("sobre", views.sobre, name="sobre"),
    path("equipe", views.equipe, name="equipe")
]
