from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreationUtilisateur

# Create your views here.

def inscriptionPage(request):
    form = CreationUtilisateur(request.POST)
    context = {'form': form}
    return render(request, 'compte/inscription.html', context)


def accesPage(request):
    context = {}
    return render(request, 'compte/acces.html', context)

