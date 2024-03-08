from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexV4, name="indexV4")
]