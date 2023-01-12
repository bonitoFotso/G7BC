from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', ProduitListView.as_view(),name = 'produit'),
    path('prod_register', ProduitCreateView.as_view(),name = 'produit_register'),
    

]
