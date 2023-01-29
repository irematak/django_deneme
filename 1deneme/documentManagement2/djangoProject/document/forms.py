from django import forms  
from django.forms import fields
from document.models import Politika, Prosedur, Talimat, Form, Liste, Tablo

class PolitikaForm(forms.ModelForm):
    class Meta:
        model = Politika
        fields="__all__"
        exclude = ['revision_number']

class ProsedurForm(forms.ModelForm):
    class Meta:
        model = Prosedur
        fields="__all__"
        exclude = ['revision_number']

class TalimatForm(forms.ModelForm):
    class Meta:
        model = Talimat
        fields="__all__"
        exclude = ['revision_number']

class FormForm(forms.ModelForm):
    class Meta:
        model = Form
        fields="__all__"
        exclude = ['revision_number']

class ListeForm(forms.ModelForm):
    class Meta:
        model = Liste
        fields="__all__"
        exclude = ['revision_number']

class TabloForm(forms.ModelForm):
    class Meta:
        model = Tablo
        fields="__all__"
        exclude = ['revision_number']

