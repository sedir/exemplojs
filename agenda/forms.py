from django import forms
from .models import Contato

class ContatoForm(forms.Form):
    nome = forms.CharField()
    telefone = forms.CharField(max_length=11)
    email = forms.CharField(max_length=40)

