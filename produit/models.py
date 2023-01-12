from django.db import models
from django.urls import reverse
# Create your models here.

class categorie(models.Model):
    nom = models.CharField( max_length=50)
    date_add = models.DateField(auto_now=True, auto_now_add=False)
    
    class Meta:
        ordering = ["-date_add"]
        
    def __str__(self):
        return self.nom

class Produit(models.Model):
    designation = models.CharField(max_length=50)
    ref_produit = models.CharField( max_length=50)
    prix = models.FloatField()
    categorie = models.ForeignKey("categorie", on_delete=models.CASCADE)
    qte_stock = models.IntegerField()
    marque = models.CharField( max_length=50)
    detail = models.CharField(max_length=50)
    img = models.ImageField( upload_to=None, height_field=420, width_field=420, max_length=None)
    slug = models.SlugField()
    date_add = models.DateField(auto_now=True, auto_now_add=False)
    
    class Meta:
        ordering = ["-date_add"]

    def get_absolute_url(self):
        return reverse("produit")
    
    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })
    
    def __str__(self):
        return self.designation
    
    
class Commande(models.Model):
    items = models.CharField(max_length=300)
    total = models.CharField(max_length=200)
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_commande']


    def __str__(self):
        return self.nom   
