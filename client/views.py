from django.shortcuts import render

from django.http import HttpResponse
from .models import Client

# Create your views here.

def client(request, pk):
    client = Client.objects.get(id=pk)
    commande = client.commande_set.all()
    commande_total = commande.count()
    context = {'client': client, 'commande': commande, 'commande_total': commande_total}
    return render(request, "client/index.html", context)