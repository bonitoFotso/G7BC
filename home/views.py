from django.shortcuts import render
from django.views.generic import *
from produit.models import *
# Create your views here.

class HomeView(View):
    template_name = 'home/home.html'
    
    def get(self,request,*args, **kwargs):
        context={
            'nom':'Home'
        }
        return render(request,self.template_name,context)

class HomeTemplateView(TemplateView):
    template_name = 'home/produit.html'
    model = Produit
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[""] = ''
        return context
    
