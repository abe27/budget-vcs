from django.urls import path

from formulavcst import views

urlpatterns = [
    path("", views.index, name="index"),
]