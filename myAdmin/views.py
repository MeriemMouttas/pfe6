
from fournisseur.models import publicite
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import TemplateView,CreateView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView,DetailView
from django.views.generic.edit import  UpdateView
from .forms import ActualiteForm, CategoriesForm, SousCategoriesForm, SubscribeForm,AproposForm, publiciteadminForm
from .models import Actualite, Categories, SousCategories,Apropos, publiciteadmin
from django.conf import settings
from django import forms
def index(request):
    temp=loader.get_template('myAdmin/dashbord.html')
    return HttpResponse(temp.render())
#Fournisseur#
def listeFournisseur(request):
    temp=loader.get_template('myAdmin/listeFournisseur.html')
    return HttpResponse(temp.render())

#Categories#
def categories(request):
    categories=Categories.objects.all()
    context={'categories':categories}
    return render(request,'myAdmin/listecategories.html',context)
def listepub(request):
    pub=publiciteadmin.objects.all()
    context={'pub':pub}
    return render(request,'myAdmin/listepublicite.html',context)
class CreateCategories(TemplateView):
    form = CategoriesForm()
    template_name = 'myadmin/categories_form.html'

    def post(self, request, *args, **kwargs):

        form = CategoriesForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse_lazy('profil', kwargs={'pk': obj.id}))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
class CategorietUpdateView(UpdateView):
    model= Categories
    fields = '__all__'
    def get_object(self):
        return Categories.objects.get(id=self.kwargs["id"])
    def form_valid(self,form):
        form.save()
        return HttpResponseRedirect('listecategories')

#sous categories#
class CreateSousCategories(TemplateView):
    form = SousCategoriesForm()
    template_name = 'myadmin/souscategories_form.html'

    def post(self, request, *args, **kwargs):

        form = SousCategoriesForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse_lazy('souscategories', kwargs={'pk': obj.id}))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
def souscategories(request,id):
    souscategories= SousCategories.objects.all().filter(Categories_id=id)
    context={'souscategories':souscategories}
    return render(request,'myAdmin/listesouscategories.html',context)
def detailsouscategorie(request,id):
    souscategories= SousCategories.objects.all().filter(Categories_id=id)
    context={'souscategories':souscategories}
    return render(request,'myAdmin/listesouscategories.html',context)
#articles#
def articles(request):
    articles= Actualite.objects.all()
    context={'articles':articles}
    return render(request,'myAdmin/listearticles.html',context)
class Articledetail(DetailView):
    model = Actualite
    template_name = 'myAdmin/detailarticle.html'
    context_object_name = 'article'
class CreateArticles(TemplateView): 
    form = ActualiteForm()
    template_name ='myadmin/article_form.html'

    def post(self, request, *args, **kwargs):

        form = ActualiteForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect('articles')

        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
class ArticletUpdateView(UpdateView):
    contenu = forms.CharField (widget=forms.Textarea) 
    model = Actualite
    fields = '__all__'
    def get_object(self):
        return Actualite.objects.get(id=self.kwargs["id"])
    def form_valid(self,form):
        form.save()
        return HttpResponseRedirect('listearticles')
#envoyez email#
def subscribe(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            recipient = form.cleaned_data.get('email')
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Success!')
            return redirect('subscribe')
    return render(request,'myAdmin/contact.html', {'form': form}) 
def propos(request):
    apropos=Apropos.objects.all()
    context={'acceuilapropos':apropos}
    return render(request,'myAdmin\Apropos.html',context)
    
class CreateApropos(CreateView):
    model = Apropos
    fields='__all__'
    def form_valid(self,form):
        model=form.save(commit=False)
        model.save()
        return HttpResponseRedirect('produit.html')
        

class AproposUpdateView(UpdateView):
    model = Apropos
    fields='__all__' 
    def get_object(self):
        return Apropos.objects.get(id=self.kwargs["id"])
    def form_valid(self,form):
        form.save()
        return HttpResponseRedirect('profil')

def PubUpdate(request,id):
    a = publiciteadmin.objects.get(id=id)
    form=publiciteadminForm(instance = a )
    pub=publiciteadmin.objects.get(id=id)
    if request.method == 'POST':
        form = publiciteadminForm(request.POST,instance=a)
        if form.is_valid():
                pub.status = form.cleaned_data['status']
                pub.save()
                return redirect('listepub')
    return render(request,'myAdmin/publiciteadmin_form.html',{'form':form})