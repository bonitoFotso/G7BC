from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import *
# Create your views here


class ProduitCreateView(CreateView):
    model =Produit
    form_class = ProduitForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main_page_title"] = 'creation de produit'
        context['panel_name'] = 'produit'
        context['panel_title'] = 'creer un produit'
        
        return context
    
class ProduitListView(ListView):
    model = Produit
    field_list = [
        'designation','detail','reference','marque','qte en stock','prix'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main_page_title"] = 'gestion de produit'
        context['panel_name'] = 'produit'
        context['panel_title'] = 'liste de produits'
        context['field_list'] = self.field_list
        return context
    