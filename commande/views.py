from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def commande(request):
    return render(request, "commande/index.html")