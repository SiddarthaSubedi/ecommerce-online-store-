from django.db import models

# Create your models here.

class Category(models.Model):
    name =models.CharField(max_length=50)
    
    
    class Meta:
        verbose_name_plural = 'categories'
        verbose_name = 'category'
    
    def __str__ (self):
        return self.name
    


class Product(models.Model):
    name = models.CharField(max_length=50)
    old_price = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'photos/products')
    all_product = models.BooleanField(default=False)
    new_arrivals = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    top_selling = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    categories= models.ManyToManyField(Category)
    
    def __str__ (self):
        return self.name