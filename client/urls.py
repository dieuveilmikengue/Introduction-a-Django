
from django.urls import path, include
from . import views

urlpatterns = [
    path("/<str:pk>/", views.client, name='client')
]
