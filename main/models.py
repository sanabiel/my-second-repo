from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.IntegerField()
    promo = models.CharField(max_length=255)
    price = models.IntegerField()
    
