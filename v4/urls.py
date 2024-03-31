from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexV4, name="indexV4"),
    path("<int:Y>/<int:m>/<int:d>/<int:H>/<int:M>/<str:title>", views.dynamic, name="dynamic")
]