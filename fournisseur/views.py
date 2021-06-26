
from django.contrib import messages
from myAdmin.models import SousCategories, publiciteadmin
from django.forms.widgets import NullBooleanSelect
from fournisseur.forms import ProduitForm
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.http.response import HttpResponseRedirect
from  .models import   Galerie, Prix, Produit,publicite,Caracteristique
from django import forms
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from myAdmin.models import Categories, SousCategories

#def a_propos(request):
    #temp=loader.get_template('Apropos.html')
    #return HttpResponse(temp.render())
#ajouter produit#
def ProduitUpdate(request,id):
    a = Produit.objects.get(id=id)
    form=ProduitForm(instance = a )
    produit=Produit.objects.get(id=id)
    if request.method == 'POST':
        form = ProduitForm(request.POST,instance=a)
        if form.is_valid():
                produit.libelle = form.cleaned_data['libelle']
                produit.Marque = form.cleaned_data['Marque']
                produit.description  = form.cleaned_data['description']
                produit.Reference = form.cleaned_data['Reference']
                produit.prix = form.cleaned_data['prix']
                produit.poid = form.cleaned_data['poid']
                produit.dure = form.cleaned_data['dure']
                produit.norme = form.cleaned_data['norme']
                souscat = form.cleaned_data['souscategorie']
                if produit.prix <= 0:
                        messages.error(request,"prix invalide")
                        return render(request,'fournisseur/produit_form.html',{'form':form})
                produit.souscategorie=SousCategories.objects.get(titre=souscat)
                produit.save()
        return HttpResponseRedirect('profil')
    else:
        return render(request,'fournisseur/produit_form.html',{'form':form})
def ajouterPrix(request):
        produit=Produit.objects.latest('updated_at','datecreation' )
        ligne=Prix.objects.create(prix=produit.prix, produit=produit.id)
        model = Produit
        return HttpResponseRedirect('prix')  
def ajouterPrixmodif(request,pk):
        produit=Produit.objects.get(id=pk)
        prixencien=Prix.objects.filter(produit=pk).latest('id')
        if(produit.prix != prixencien.prix):
            ligne=Prix.objects.create(prix=produit.prix, produit=produit.id)
        return HttpResponseRedirect('profil1')  
class ajouterGalerie(CreateView):
     model=Galerie
     fields='__all__'
     def form_valid(self,form):
          model=form.save(commit=False)
          model.save()
          return HttpResponseRedirect('galerie') 


class ProduitDeleteView(DeleteView):
    template_name = 'fournisseur/produit_delete.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Produit, id=id_)

    def get_success_url(self):
        return reverse('produits') 
def detail(request,pk):
    produit=Produit.objects.all().filter(id=pk)
    caracteristique=Caracteristique.objects.all().filter(produit_id=pk)
    context={'produit':produit,
    'caracteristique':caracteristique,
    }
    return render(request,'fournisseur/detailproduit.html',context)
def produits(request):
    produits=Produit.objects.all().order_by('-prix')
    context={'produits':produits}
    return render(request,'fournisseur\produits.html',context)
def produitscertifie(request):
    produits=Produit.objects.all().filter(norme__isnull=False)
    context={'produits':produits}
    return render(request,'fournisseur\produits.html',context)
def  produitsgarenti(request):
    produits=Produit.objects.all().filter(dure__isnull=False)
    context={'produits':produits}
    return render(request,'fournisseur\produits.html',context)


#  publicite    
class PubliciteCreate(CreateView):
    model = publicite
    fields=('image',)
    def form_valid(self,form):
        model=form.save(commit=False)
        model.save()
        return HttpResponseRedirect('profil')
def ajouterpub(request):
        pub=publicite.objects.latest('id')
        pubadmn=publiciteadmin.objects.create(image=pub.image,status=pub.status)
        return HttpResponseRedirect('profil1')  
class CaracteristiqueCreate(CreateView):
    model = Caracteristique
    fields='__all__'
    def form_valid(self,form):
        model=form.save(commit=False)
        model.save()
        return HttpResponseRedirect('detail')
class CaracteristiqueUpdateView(UpdateView):
    model = Caracteristique
    fields='__all__' 
    def get_object(self):
        return Caracteristique.objects.get(id=self.kwargs["id"])
    def form_valid(self,form):
        form.save()
        return HttpResponseRedirect('profil')

def historique(request,pk):
    historiques=Prix.objects.all().filter(produit=pk)
    context={'historiques':historiques}
    return render(request,'fournisseur/historique.html',context)

def sample_view(request): 
    current_user = request.user.id
    c=current_user
    return c
def ProduitCreate(request):
    form= ProduitForm()
    current_user = request.user.id
    if request.method == 'POST':
        form = ProduitForm(request.POST,request.FILES)
        if request.user.user_type=="3":
            if form.is_valid():
                libelle = form.cleaned_data['libelle']
                Marque = form.cleaned_data['Marque']
                description  = form.cleaned_data['description']
                Reference = form.cleaned_data['Reference']
                prix = form.cleaned_data['prix']
                poid = form.cleaned_data['poid']
                dure = form.cleaned_data['dure']
                norme = form.cleaned_data['norme']
                souscategorie = form.cleaned_data['souscategorie']
                souscat=SousCategories.objects.get(titre=souscategorie)
                if prix <= 0:
                        messages.error(request,"prix invalide")
                        return HttpResponseRedirect(reverse("createproduit"))
                Produit.objects.create(libelle=libelle,Marque=Marque,description=description,Reference=Reference,
                prix=prix, poid=poid ,dure=dure,norme=norme,souscategorie_id =souscat.id,fournisseur_id=current_user)
                 
                return HttpResponseRedirect('profil')
        
    return render(request,'fournisseur/produit_form.html',{'form':form})