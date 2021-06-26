from  .models import Actualite, Categories, SousCategories,Apropos, publiciteadmin
from django.forms import ModelForm, fields
from django import forms


class CategoriesForm(ModelForm): 
  
    class Meta: 
        model = Categories 
        fields = ['titre'] 
class SousCategoriesForm(ModelForm): 
      class Meta: 
        model = SousCategories 
        fields = '__all__'
class ActualiteForm(ModelForm): 
      contenu = forms.CharField (widget=forms.Textarea) 
      class Meta: 
           model = Actualite
           fields = '__all__'

class SubscribeForm(forms.Form):
    email = forms.EmailField()
    subject=forms.CharField ()
    message = forms.CharField (widget=forms.Textarea) 
class AproposForm(ModelForm):
    class Meta:
        model=Apropos
        fields='__all__'
class publiciteadminForm(ModelForm):
    class Meta:
        model=publiciteadmin
        fields=('status',)