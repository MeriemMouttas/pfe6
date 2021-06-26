

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class CustomUser(AbstractUser):
    user_type_data=((1,"HOD"),(2,"Client"),(3,"Fournisseur"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    confirm_password=models.TextField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Clients(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    confirm_password=models.TextField(max_length=50)
    adresse=models.TextField(max_length=50)
    wilaya=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    fcm_token=models.TextField(default="")
    objects=models.Manager()


class Fournisseurs(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    confirm_password=models.TextField(max_length=50)
    adresse=models.TextField()
  
    wilaya=models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    nom_entreprise = models.CharField(max_length=50)
    num_registre = models.CharField(max_length=20)
    site = models.CharField(max_length=25)
    forme_juridique = models.CharField(max_length=25)
    activite = models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    fcm_token=models.TextField(default="")
    objects = models.Manager()

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance,confirm_password="")
        if instance.user_type==2:
            Clients.objects.create(admin=instance,confirm_password="",wilaya="")
        if instance.user_type==3:
            Fournisseurs.objects.create(admin=instance,confirm_password="",adresse="",wilaya="",phone="",nom_entreprise="",num_registre="",site="",forme_juridique="",activite="")

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminhod.save() 
    if instance.user_type==2:
        instance.clients.save()
    if instance.user_type==3:
        instance.fournisseurs.save()
class DemandesProduits(models.Model):
    user=models.ForeignKey("mySite.CustomUser",on_delete=models.CASCADE)
    titre=models.CharField(max_length=255)
    detail=models.CharField(max_length=255)
    sous_categorie=models.ForeignKey("myAdmin.SousCategories",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
class ContactMessage(models.Model):
    STATUS = [
    ('Nouveau', 'Nouveau'),
    ('Lis', 'Lis'),
    ('Fermé', 'Fermé'),
]
    nom = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    objet = models.CharField(max_length=50)
    message = models.TextField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    note = models.CharField(max_length=140, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model ):
    
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
       
    )
    produit_id=models.ForeignKey("fournisseur.Produit",on_delete=models.CASCADE)
    user_id = models.ForeignKey("mySite.CustomUser", on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250,blank=True)
    notation = models.IntegerField(default="1")
    status=models.CharField(max_length=10,choices=STATUS, default='New')
    create_at=models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default=1)
    objects = models.Manager()

    def __str__(self):
        return self.subject


