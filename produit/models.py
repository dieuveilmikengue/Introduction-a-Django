from django.db import models

# Create your models here.

class Tag(models.Model):
    nom = models.CharField(max_length=50, null=True)

    # Une fonction qui retourne le nom dans la base de donnée
    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=50, null=True)
    prix = models.FloatField(null=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)

    # Une fonction qui retourne le nom dans la base de donnée
    def __str__(self):
        return self.nom