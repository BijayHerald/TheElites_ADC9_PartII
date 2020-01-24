from django.db import models
from django.urls import reverse
import datetime
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
    



class Product(models.Model):
    name = models.CharField(max_length=100)
    Fullprice = models.DecimalField(max_digits=10, decimal_places=2)
    Discountprice = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to='products/jpg',blank=True)
    #brand = models.ForeignKey(Brand, on_delete = models.CASCADE, related_name = "brands")


    class Meta:
        ordering=('name',)
        index_together=('id',)#'slug')

