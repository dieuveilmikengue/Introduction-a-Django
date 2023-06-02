from django.urls import path, include
from . import views

urlpatterns = [
    path("inscription", views.inscriptionPage, name='inscription'),
    path("acces", views.accesPage, name='acces'),
]
