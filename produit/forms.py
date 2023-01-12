from .models import *
from django import forms

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'
        Widget = {
            'designation' : forms.TextInput(attrs={'class':'nom','name':'nom'}),
            'detail' : forms.TextInput(attrs={'class':'nom','name':'detail'}),
            'ref_produit' : forms.TextInput(attrs={'class':'nom','name':'detail'}),
            'marque' : forms.TextInput(attrs={'class':'nom','name':'detail'}),
            'prix' : forms.NumberInput(attrs={'class':'nom','name':'detail'}),
            'qte_stock' : forms.NumberInput(attrs={'class':'nom','name':'detail'}),
        }