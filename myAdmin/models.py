from django.db import models
import datetime
from mySite.models import CustomUser
from django.db.models.deletion import CASCADE

class Categories(models.Model):
    titre = models.CharField(max_length=50,blank=False,unique=True)
    pass
    def __str__(self):
    
            return self.titre
class SousCategories(models.Model):
    titre = models.CharField(max_length=50,blank=False)
    Categories = models.ForeignKey(Categories, on_delete=models.CASCADE,)
    pass
    def __str__(self):
            return self.titre
class Actualite(models.Model):
    titre = models.CharField(max_length=50,blank=False)
    description = models.CharField(max_length=150,blank=False)
    contenu = models.TextField()
    image = models.ImageField(upload_to='images/articles',blank=False)

class Apropos(models.Model):
    description = models.TextField(max_length=250)
    logo= models.ImageField(upload_to='images/logo')
    video = models.FileField(upload_to='videos/')
    libelle =models.CharField(max_length=25)


class publiciteadmin(models.Model):
    image = models.ImageField(upload_to='images/publicites',blank=False)
    status=models.CharField(max_length=20,default="en attente")
   

    def __str__(self):
            return self.image
class AppelOffert(models.Model):
    titre=models.CharField(max_length=50)
    description=models.TextField()
    date=models.DateField()
    status=models.CharField(max_length=45)

# Create your models here.
