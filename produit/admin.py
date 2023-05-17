from django.contrib import admin

from .models import Produit
from .models import Tag

# Register your models here.

admin.site.register(Produit)
admin.site.register(Tag)