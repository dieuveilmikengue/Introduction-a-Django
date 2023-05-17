from django.db import models

# Create your models here.

class Client(models.Model):
    nom = models.CharField(max_length=50, null=True)
    telephone = models.CharField(max_length=100, null=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom