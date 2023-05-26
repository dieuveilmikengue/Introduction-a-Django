
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.commande),
    path("ajout_commande/", views.ajouter_commande, name="ajout_commande"),
    path("modifier_commande/<str:pk>", views.modifier_commande, name="modifier_commande"),
    path("supprimer_commande/<str:pk>", views.supprimer_commande, name="supprimer_commande")
]
