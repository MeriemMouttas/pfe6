from django.shortcuts import render
from django.template import loader
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render
from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Avg, Count, Q, F
from mySite.EmailBackEnd import EmailBackEnd
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
import requests
import json
from django.views.decorators.csrf import csrf_exempt
import os
from django.dispatch import receiver
from fournisseur.models import publicite,Galerie, Produit
from myAdmin.models import SousCategories,Categories
from mySite.models import CustomUser,Clients
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from PFE import settings

def detailProduit(request,id):
    produits=Produit.objects.all().filter(id=id)
    image=Galerie.objects.all().filter(produit_id=id)
    context={
    'produits':produits,
    'image':image,}
    return render(request,'mySite/product-page.html',context)
    
def accueil(request):
    cat=Categories.objects.all()
    souscat=SousCategories.objects.all()
    pub=publicite.objects.all()
    context={'souscat':souscat,
    'cat':cat,
    'pub':pub, }
    return render(request,'mySite/index.html',context)
# Create your views here.

def registerPage(request):
    form=UserCreationForm()
    context={}
    return render(request,'mySite\register.html',context)

def signup_admin(request):
    return render(request,"signup_admin_page.html")

def signup_fournisseur(request):
  
   return render(request,"signup_fournisseur_page.html")
def signup_client(request):
    return render(request,"signup_client_page.html")

def do_admin_signup(request):
 if request.method=='POST':
    username=request.POST.get("username")
    email=request.POST.get("email")
    first_name=request.POST.get("first_name")
    last_name=request.POST.get("last_name")
    password=request.POST.get("password")
    confirm_password=request.POST.get("confirm_password")
   
    if password==confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request,"Username existe")
                return HttpResponseRedirect(reverse("signup_admin"))
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request,"email existe")
                return HttpResponseRedirect(reverse("signup_admin"))
            else:
                user=CustomUser.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name,user_type=1)
                user.adminhod.confirm_password=confirm_password
                user.save()
                messages.success(request,"Administrateur créé avec succès")
                return HttpResponseRedirect(reverse("show_login"))
    else:
            messages.error(request,"Échec de la création du administrateur")
            return HttpResponseRedirect(reverse("signup_admin"))
    
 return HttpResponseRedirect(reverse("show_login"))

def do_client_signup(request):
 if request.method=='POST':
    username=request.POST.get("username")
    first_name=request.POST.get("first_name")
    last_name=request.POST.get("last_name")
    email=request.POST.get("email")
    password=request.POST.get("password")
    adresse=request.POST.get("adresse")
    wilaya=request.POST.get("wilaya")
    phone=request.POST.get("phone")
    confirm_password=request.POST.get("confirm_password")
    if password==confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request,"Username existe")
                return HttpResponseRedirect(reverse("signup_client"))
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request,"email existe")
                return HttpResponseRedirect(reverse("signup_client"))
            else:
                user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
                user.clients.confirm_password=confirm_password
                user.clients.adresse=adresse
                user.clients.wilaya=wilaya
                user.clients.phone = phone
                user.save()
                messages.success(request,"Client créé avec succès")
                return HttpResponseRedirect(reverse("show_login"))
    else:
        messages.error(request,"Échec de la création du client")
        return HttpResponseRedirect(reverse("signup_client"))
 return HttpResponseRedirect(reverse("show_login"))

def do_signup_fournisseur(request): 
 if request.method=='POST':
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    adresse = request.POST.get("adresse")
    wilaya=request.POST.get("wilaya")
    forme_juridique = request.POST.get("forme_juridique")
    phone = request.POST.get("phone")
    nom_entreprise = request.POST.get("nom_entreprise")
    num_registre = request.POST.get("num_registre")
    site = request.POST.get("site")
    activite = request.POST.get("activite")
    confirm_password=request.POST.get("confirm_password")

    logo = request.FILES.get('logo')
    fs = FileSystemStorage()
    filename = fs.save(logo.name , logo)
    logo_url = fs.url(filename)

    catalogue = request.FILES.get('catalogue')
    fs = FileSystemStorage()
    filename = fs.save(catalogue.name , catalogue)
    catalogue_url = fs.url(filename)
    libelle = request.POST.get("libelle")
    marque = request.POST.get("marque")
    reference = request.POST.get("reference")

    if password==confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request,"Username existe")
                return HttpResponseRedirect(reverse("signup_fournisseur"))
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request,"Email existe déja")
                return HttpResponseRedirect(reverse("signup_fournisseur"))
                
            else:
                user = CustomUser.objects.create_user(username=username, password=password, email=email, last_name=last_name,first_name=first_name, user_type=3)
                user.fournisseurs.confirm_password=confirm_password
                user.fournisseurs.adresse = adresse
                user.fournisseurs.wilaya=wilaya
                user.fournisseurs.forme_juridique = forme_juridique
                user.fournisseurs.phone = phone
                user.fournisseurs.nom_entreprise = nom_entreprise
                user.fournisseurs.num_registre = num_registre
                user.fournisseurs.site = site
                user.fournisseurs.activite = activite 
                user.fournisseurs.logo = logo_url
                user.fournisseurs.catalogue = catalogue_url
                user.fournisseurs.libelle=libelle
                user.fournisseurs.marque=marque
                user.fournisseurs.reference=reference

                user.save()
                messages.success(request,"Fournisseur créé avec succès")
                return HttpResponseRedirect(reverse("show_login"))
    else:
        messages.error(request,"Échec de la création du fournisseur")
        return HttpResponseRedirect(reverse("signup_fournisseur"))

 return HttpResponseRedirect(reverse("show_login"))
  
def ShowLoginPage(request):
    return render(request,"mySite/login_page.html")
def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        captcha_token=request.POST.get("g-recaptcha-response")
        cap_url="https://www.google.com/recaptcha/api/siteverify"
        cap_secret="6LeWtqUZAAAAANlv3se4uw5WAg-p0X61CJjHPxKT"
        cap_data={"secret":cap_secret,"response":captcha_token}
        cap_server_response=requests.post(url=cap_url,data=cap_data)
        cap_json=json.loads(cap_server_response.text)

        if cap_json['success']==False:
            messages.error(request,"invalide! Réessayez ")
            return HttpResponseRedirect("/")
        user=EmailBackEnd.authenticate(request,username=request.POST.get("username"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            current_user =request.user
            if user.user_type=="1":
                return HttpResponseRedirect(reverse("profil"))
                
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("client_profil"))
            else:
                return HttpResponseRedirect(reverse("createproduit"))
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")  
    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect("accueil")
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
         data = ContactMessage()
         data.nom = form.cleaned_data['nom']
         data.email = form.cleaned_data['email']
         data.objet= form.cleaned_data['objet']
         data.message = form.cleaned_data['message']
         data.save()
         messages.success(request,"votre message est recu.")
         return render(request,"contactez_nous.html",{'data.nom':data.nom})
            
    temp=loader.get_template('contactez_nous.html')
    form = ContactForm
    context={'form':form }
    return HttpResponse(temp.render())    
# Create your views here.

#commentaire                   sayi darwag!!!!!!!!!!!!!!!! wsm sayi 

@login_required(login_url='/')
def addcomment(request,id):      
    form = CommentForm()
    user=CustomUser.objects.get(id=request.user)
    if request.method == 'POST': 
        form = CommentForm(request.POST)
        if request.user.user_type=="2":
            if form.is_valid():
                # create relation with model
                subject = form.cleaned_data['subject']
                comment = form.cleaned_data['comment']
                notation = form.cleaned_data['notation']
                produit_id=id
                save() 
                messages.success(request, "Your review has ben sent. Thank you for your interest.")
                return HttpResponseRedirect(url)
            return HttpResponseRedirect(url)
        return HttpResponseRedirect(reverse("show_login"))
#evaluation

def client_profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    client=Clients.objects.get(admin=user)
    return render(request,"profile.html",{"user":user,"client":client})
    
def client_profile_save(request):
    if request.method!="POST":
        return render(request,"modifier_profil.html")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        adresse=request.POST.get("adresse")
        wilaya=request.POST.get("wilaya")
        phone=request.POST.get("phone")
        password=request.POST.get("password")
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            customuser.email=email
            if password!=None and password!="":
                customuser.set_password(password)
            customuser.save()

            client=Clients.objects.get(admin=customuser.id)
            client.adresse=adresse
            client.wilaya=wilaya
            client.phone=phone
            client.save()
            messages.success(request, "Profil mis à jour avec succès")
            return render(request, 'profile.html')
        except:
            messages.error(request, "Échec de la mise à jour du profil")
            return render(request, 'modifier_profil.html')
def user_password(request):
    if request.method!="POST":
        return render(request,"modifier_profil.html")
    else:
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.password(password)
            customuser.save()
            client=Clients.objects.get(admin=customuser.id)
            client.adresse=adresse
            messages.success(request, "Profil mis à jour avec succès")
            return render(request, 'profile.html')
        except:
            messages.error(request, "Échec de la mise à jour du profil")
            return render(request, 'password_profil.html')
        

def ajoute_produit_site(request):
    prds=DemandesProduits.objects.all()
    return render(request,"demande_produit_site.html",{"prds":prds})

def client_ajoute_produit(request):
    sous_categories=SousCategories.objects.all()
    return render(request,"demande_produit.html",{"sous_categories":sous_categories})

@login_required(login_url='/')

       
def appel_offres(request):
    return render(request,"mySite/appel _offres.html")
def search(request):
    if request.method == 'POST': # check post
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'] # get form input data
            catid = form.cleaned_data['catid']
            if catid==0:
                products=Produit.objects.filter(libelle__contains=query)  #SELECT * FROM product WHERE title LIKE '%query%'
            else:
                cat=SousCategories.objects.get(Categories_id=catid)
                products = Produit.objects.filter(libelle__contains=query,souscategorie_id=cat.id)

            category = Categories.objects.all()
            context = {'products': products, 'query':query,
                       'category': category }
            return render(request, 'mySite/search_products.html', context)

    return HttpResponseRedirect('/')
def filter_data(request):
	categories=request.GET.getlist('Categories[]')
	brands=request.GET.getlist('brand[]')
	sizes=request.GET.getlist('size[]')
	minPrice=request.GET['minPrice']
	maxPrice=request.GET['maxPrice']
	allProducts=Produit.objects.all().order_by('-id').distinct()
	allProducts==Produit.filter(produit__prix__gte=minPrice)
	allProducts==Produit.filter(produit__prix__lte=maxPrice)
	if len(categories)>0:
		allProducts==Produit.filter(category__id__in=categories).distinct()
	t=render_to_string('ajax/product-list.html',{'data':allProducts})
	return JsonResponse({'data':t})
def tousproduit(request,pk):
    cat=Categories.objects.all()
    souscat=SousCategories.objects.all()
    produits=Produit.objects.all().filter(souscategorie_id=pk)
    image=Galerie.objects.all().distinct('produit_id')
    paginator = Paginator(produits, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'souscat':souscat,
    'cat':cat,
    'produits':produits,
    'image':image,
    'page_obj': page_obj}
    return render(request,'mySite/products.html',context)