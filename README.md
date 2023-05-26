# Initiation au FrameWork Django

## I- Commencer d'abord par installer Python:

https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe

## II- Installer Django

    pip install django

### 1- Creation du Projet

    django-admin startproject nomDuprojet

Note: Vous devez éviter de nommer vos projets en utilisant des noms réservés de Python ou des noms de composants de Django. Cela signifie en particulier que vous devez éviter d’utiliser des noms comme django (qui entrerait en conflit avec Django lui-même) ou test (qui entrerait en conflit avec un composant intégré de Python).

### 2- Lancer le projet

    py manage.py runserver

Note: Rassurez vous d'etre dans le repertoire nomduprojet:
<..../nomduprojet> py manage.py runserver

## III- Gestion des urls

1- On ajoute les urls de nos page dans le fichier urls.py du projet principal
On aura ceci:

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("", include("produit.urls")), 
        path("commande", include("commande.urls")),
        path("client", include("client.urls")),
    ]

ou les 3 dernieres lignes du tableau urlpatterns sont des urls qu'on a ajouté

2- On crée un fichier urls.py dans chacun de nos composants par exemple ici on a crée 3 dossiers: client, commande et produit
on ajoute le code ci dessous dans chacun de nos fichiers urls.py qu'on a crée en personalisant par rapport a nos pages:

    path("", views.home) pour la page home qui est la page d'accueille, ici on a choisit la page produit comme page d'accueille
    path("commande", views.commande) pour la page des commandes
    path("client", views.client) pour la page des clients

    from django.urls import path, include
    from . import views

    urlpatterns = [
        path("", views.home)
    ]

3- On met le code qui sera affiché dans l'ecran avec les fichiers views.py de chaque composant

    #On fait appel a nos modules
    from django.shortcuts import render
    from django.http import HttpResponse

    #On écrit notre page: page de commande comme exemple
    def list_commande(request):
        return HttpResponse("Liste des commandes")

## IV- L'utilisation des templates

1- On importe le os dans notre fichier settings.py de notre dossier projet et on ajoute le templates

    import os 
    .........................
    .........................
    .........................
    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [os.path.join(BASE_DIR, "templates")],  #c'est la ligne qu'on a modifiée
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

2- On crée notre dossier templates ou on mettrai nos pages

a- On crée une page html qu'on appelera ici par main.html qui va contenir tous nos composants des pages    1- dans ce fichier, on ecrit toute la structure html et les liens vers css, javascript et nos composantes des pages (Navbar, Section, Footer)
2- on crée le fichier navbar.html dans templates qui va contenir notre en tete pour toutes les pages
3- on crée le fichier footer.html dans templates qui va contenir le pieds de page pour toutes les pages

b- On crée un dossier produit dans le dossier templates pour recuperer les composantes de la page d'accueille
    1- on créee le fichier html qui sera considéré comme page d'accueille, index.html par exemple dans le dossier templates/produit
    2- dans ce fichier on mettra juste le contenu ou section de la page d'accueille

c- On crée un dossier client dans le dossier templates pour recuperer les composantes de la page d'accueille
1- on créee le fichier html qui sera considéré comme page client, index.html par exemple dans le dossier templates/client
2- dans ce fichier on mettra juste le contenu ou section de la page client

d- On crée un dossier commande dans le dossier templates pour recuperer les composantes de la page d'accueille
1- on créee le fichier html qui sera considéré comme page commande, index.html par exemple dans le dossier templates/commande
- dans ce fichier on mettra juste le contenu ou section de la page commande

    Ici on va travailler avec Bootsrap

3- On repart dans nos dossiers produit, client et commande de notre projet principal

a- On modifie le fichier view.py de notre dossier produit en recuperant le chemin de notre page d'accueille dans produit du templates
        .....................
        .....................
        .....................
        def home(request):
            return render(request, "produit/index.html")

    a- On modifie le fichier view.py de notre dossier client en recuperant le chemin de notre page client dans client du templates
        .....................
        .....................
        .....................
        def home(request):
            return render(request, "client/index.html")

    a- On modifie le fichier view.py de notre dossier pcommande en recuperant le chemin de notre page commande dans commande du templates
        .....................
        .....................
        .....................
        def home(request):
            return render(request, "commande/index.html")


## V- Manipuler les templates statics

### 1- Créer un dossier static dans le projet principal projet/static


a- Créer un dossier css ou sera stocker les fichiers css, pour l'exemple on a crée un fichier style.css dans le dossier css crée
le chemin dans le fichier main.html: <link rel="stylesheet" href="{% static 'css/style.css' %}">

b- Créer un dossier js ou sera stocker les fichiers js, pour l'exemple on a crée un fichier style.js dans le dossier css crée
le chemin dans le fichier main.html: <script src="{% static 'js/script.js' %}"></script>

c- Créer un dossier images ou sera stocker les images
<img src="{% static 'images/objet.png' %}">


2- Repartez dans settings du projet vous allez remarquer que la ligne < STATIC_URL = "static/" > a été génerée automatiquement

a- On crée une nouvelle ligne < STATICFILES_DIRS=[os.path.join(BASE_DIR, 'static')] > qui va recuperer nos fichiers css et js

b- On crée une autre ligne < MEDIA_URL='/images/' > qui va recuperer les medias


## VI- Les modeles 

Preparer comment les données seront stocker dans notre base de données

1- 
a- On crée une class produit dans le fichier models.py du dossier produit qui sera consideré comme notre model avec des champs comme suit:

        class Produit(models.Model):
            nom = models.CharField(max_length=50, null=True)
            prix = models.FloatField(null=True)
            date_creation = models.DateTimeField(auto_now_add=True, null=True)

            # Une fonction qui retourne le nom dans la base de donnée
            def __str__(self):
                return self.nom

b- On crée une class commande dans le fichier models.py du dossier commande qui sera consideré comme notre model avec des champs comme suit:

        class Commande(models.Model):
            STATUS = (('en instance', 'en instance'),
                    ('non livré', 'non livré'),
                    ('livré', 'livré'))
            # produit = 
            # client = 
            statuts = models.CharField(max_length=150, null=True, choices=STATUS)
            date_creation = models.DateTimeField(auto_now_add=True, null=True)

            def __str__(self):
                return self.nom

c- On crée une class client dans le fichier models.py du dossier client qui sera consideré comme notre model avec des champs comme suit:

        class Client(models.Model):
            nom = models.CharField(max_length=50, null=True)
            telephone = models.CharField(max_length=100, null=True)
            date_creation = models.DateTimeField(auto_now_add=True, null=True)

            def __str__(self):
                return self.nom

2- On fait la migration de nos class dans dons chacun de nos composant et on verifie nos champs dans le fichier 0001_initial.py qui sera crée dans le dossier migration de nos dossiers
command: 
py manage.py makemigrations

La class va correspondre a ca dans le fichier 0001_initial.py, ci-dessous c'est pour la le model client
0001_initial.py

    class Migration(migrations.Migration):

        initial = True

        dependencies = []

        operations = [
            migrations.CreateModel(
                name="Client",
                fields=[
                    (
                        "id",
                        models.BigAutoField(
                            auto_created=True,
                            primary_key=True,
                            serialize=False,
                            verbose_name="ID",
                        ),
                    ),
                    ("nom", models.CharField(max_length=50, null=True)),
                    ("telephone", models.CharField(max_length=100, null=True)),
                    ("date_creation", models.DateTimeField(auto_now_add=True, null=True)),
                ],
            ),
        ]

3- Une fois qu'on a verifier nos class migrées n'ont pas d'erreur, on peut l'envoyer dans la base de données du projet on utilisant la commande:
py manage.py migrate

4- On crée un utilisateur pour se connecter a la base de données du systeme django on utilisant la commande:
py manage.py createsuperuser
................identiant
...............adress mail
...............mot de passe

pour se connecter à la base, vous utilisez l'url: 
localhost/admin

## VII- Les relations entre les bases de données

1- One to Many
Un client peut commander plusieurs produits et faire plusieurs commandes 
Un produit peut se retrouver dans plusieurs commande

a- On recupère notre model commande:
On importe les models Client et Poduit:

    from client.models import Client
    from produit.models import Produit

On ajoute les champs client et produit:

    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    produit = models.ForeignKey(Produit, null=True, on_delete=models.SET_NULL)

2- Many to many
Un produit peut avoir plusieurs tag

a- On recupère notre models Produit
On crée une class Tag pour ajouter des tag:

    class Tag(models.Model):
        nom = models.CharField(max_length=50, null=True)

        # Une fonction qui retourne le nom dans la base de donnée
        def __str__(self):
            return self.nom
    
b- On importe le tag dans notre admin.py du Produit:

        from django.contrib import admin
        from .models import Produit
        from .models import Tag

        # Register your models here.

        admin.site.register(Produit)
        admin.site.register(Tag)


## VIII- Afficher les donnees dans le site



## IX- Implementation des Fonctionnalité CRUD




