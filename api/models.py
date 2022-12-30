from django.db import models

# Create your models here.

size = (("10","10"),("20","20"),("30","30"))

quality = (('high','high'),('low','low'),('medium','medium'))

colors = (('red','red'),('blue','blue'),('green','green'),('black','black'))

class Products(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    unique_code = models.CharField(max_length=10, unique=True)
    size = models.CharField(max_length=10, choices=size)
    quality = models.CharField(max_length=40, choices=quality)
    

    
class ProductColor(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name = 'color')
    color = models.CharField(max_length=50, choices=colors)

class ProductImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE,related_name = 'image')
    image = models.ImageField(upload_to='images/')