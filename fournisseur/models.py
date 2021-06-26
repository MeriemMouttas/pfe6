import datetime
from mySite.models import CustomUser
import fournisseur
from myAdmin.models import Categories, SousCategories
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from PIL import Image as PilImage
from django.core.exceptions import ValidationError



class Produit(models.Model):
    image =models.ImageField(upload_to='images/produits',blank=False)
    fiche=models.FileField(upload_to='fiche_technique',blank=True)
    libelle = models.CharField(max_length=30,blank=False,unique=True)
    Marque = models.CharField(max_length=15,blank=False)
    description = models.TextField(blank=False)
    Reference=models.CharField(max_length=20,blank=False)
    prix = models.FloatField(blank=False)
    poid=models.FloatField(default=0, blank=True)
    dure=models.CharField(max_length=20, blank=True,null=True)
    norme=models.CharField(max_length=20,null=True,blank=True)
    souscategorie=models.ForeignKey(SousCategories,on_delete=CASCADE) 
    fournisseur=models.ForeignKey(CustomUser,on_delete=CASCADE)
    datecreation = models.DateTimeField('date',auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    pass
    def __str__(self):
            return self.libelle

class Caracteristique(models.Model):
    produit=models.ForeignKey(Produit,on_delete=CASCADE) 
    titre= models.CharField(max_length=30,blank=False)
    detail=models.CharField(max_length=30,blank=False)
    def __str__(self):

            return self.libelle
class Prix(models.Model):
    prix=models.FloatField()
    produit=models.PositiveIntegerField()
    datecreation = models.DateTimeField('date',auto_now=True)
    def __str__(self):
            return self.prix
# Create your models here.
class publicite(models.Model):
    image = models.ImageField(upload_to='images/publicites',blank=False)
    status=models.CharField(max_length=20,default="en attente")
   

    def __str__(self):
            return self.image
class Galerie(models.Model):
    image = models.ImageField(upload_to='images/Galerie',blank=False)
    produit=models.ForeignKey(Produit,on_delete=CASCADE)
class produitpromo(models.Model):
    produit=models.ForeignKey(Produit,on_delete=CASCADE)
    prix=models.FloatField()

