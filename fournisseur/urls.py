
from django import urls
from django.urls import path,include
from . import views
 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

 #path('A_propos/',views.a_propos,name='A_propos'), 
 
 # produit#
 path('createproduit/',views.ProduitCreate,name='createproduit'),
  path('produitcertifie/',views.produitscertifie,name='produitcertifie'),
  path('produitgarenti/',views.produitsgarenti,name='produitgaranti'),
 path('createproduit/profil',views.ajouterPrix,name='ajouterPrix'),

path('update_produit/<int:id>/', views.ProduitUpdate, name="ProduitUpdateView"),
path('produits',views.produits,name="produits"),
 path('<int:id>/delete/',views.ProduitDeleteView.as_view(), name='produitDelete'),
path('detailproduit/<int:pk>/',views.detail, name='detailproduit'),

 path('update_produit/<int:pk>/profil',views.ajouterPrixmodif,name='ajouterPrix'),
 path('historique/<int:pk>/',views.historique, name='historique'),
path('createproduit/prix/',views.ajouterGalerie.as_view(),name='galeriecaracteristique'),
 path('createproduit/prix/galerie',views.produits,name="produits"),


 ##produit caracteristique :
  path('createcaracteristique/',views.CaracteristiqueCreate.as_view(),name='createcaracteristique'),
  path('createcaracteristique/detail',views.produits,name="produits"),
  path('update_produit/<int:pk>/profil1',views.detail,name="produits"),
#pub
 path('createpublicite/',views.PubliciteCreate.as_view(),name='PubliciteCreate'),
  path('createpublicite/profil',views.ajouterpub,name='createpublicite'),
  path('createpublicite/profil1',views.produits),



 ]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)