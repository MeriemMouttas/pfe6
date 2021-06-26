from django.forms import ModelForm
from django import forms
from .models import ContactMessage,Comment

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    catid = forms.IntegerField()

class ContactForm(ModelForm):

    class Meta:
        model=ContactMessage
        fields=['nom','email','objet','message']
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'notation']