
from django.urls import path
from . import views
from myAdmin import views
from mySite import views
from django.urls import path, include

urlpatterns = [
    
    path('accueil',views.accueil,name='A_propos'), 
    path('register/',views.registerPage ,name='register'),
    path('inscription_admin',views.signup_admin,name="signup_admin"),
    path('inscription_fournisseur',views.signup_fournisseur,name="signup_fournisseur"),
    path('inscription_client',views.signup_client,name="signup_client"),
    path('do_admin_signup',views.do_admin_signup,name="do_admin_signup"),
    path('do_client_inscription',views.do_client_signup,name="do_client_signup"),
    path('do_signup_fournisseur',views.do_signup_fournisseur,name="do_signup_fournisseur"),
    path('',views.ShowLoginPage,name="show_login"),
    path('doLogin',views.doLogin,name="do_login"),
    path('logout_user', views.logout_user,name="logout"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('contactez_nous/',views.contact ,name='contact'),
    
    path('addcomment/',views.addcomment,name='addcomment'),
    #client 
    path('client_profile',views.client_profile, name="client_profil"),
    path('client_profile_save', views.client_profile_save, name="client_profile_save"),
    path('ajouter_produit', views.client_ajoute_produit,name="ajouter_produit"),

    path('appel_offres/',views.appel_offres,name="appel_offres"),
    path('demande_produits/', views.ajoute_produit_site , name='ajoute_produit_site'),
    path('lesproduits/<int:pk>/',views.tousproduit,name='lesproduits'),
    path('accueil',views.accueil,name='A_propos'),
    path('search/', views.search, name='search'),
    path('filter-data/',views.filter_data,name='filter_data'),
    path('detailProduit/<int:id>/',views.detailProduit,name='detailProduit'),
 ]