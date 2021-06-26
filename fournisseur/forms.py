import datetime
from django import forms
from  .models import  Produit, produitpromo, publicite
from django.forms import ModelForm
from django.utils import timezone

class PubliciteForm(ModelForm):
    class Meta:
        model = publicite
        fields= ('image',)
class  ProduitForm(ModelForm):
    class Meta:
        model=Produit
        fields=('Marque','libelle','fiche','description','Reference','prix','poid','dure','norme','souscategorie')