from django.db import models
from django.urls import reverse
import datetime
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
    
    def is_valid_category(self):
        return self.name!=None



class Meta:
    ordering = ('name',)
    verbose_name = 'category'
    verbose_name_plural = 'categories'



    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('mobileStore:product_list_by_category', args=[self.slug])






class Product(models.Model):
    name = models.CharField(max_length=100)
    Fullprice = models.DecimalField(max_digits=10, decimal_places=2)
    Discountprice = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to='products/jpg',blank=True)
    #brand = models.ForeignKey(Brand, on_delete = models.CASCADE, related_name = "brands")


    class Meta:
        ordering=('name',)
        index_together=('id',)#'slug')



    def __str__(self):
        return self.name

    def is_valid_Fullamount(self):
        return self.Fullprice

    # def is_valid_img(self):
    #     return self.image

class Customer(models.Model):
    cus_name = models.CharField(max_length=50)
    cus_address = models.CharField(max_length=60)
    cus_phone = models.IntegerField()
    product = models.ManyToManyField(Product)

    def is_valid_number(self):
        return self.cus_phone



class Order(models.Model):
    order_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name = "customers")
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = "products")

    def is_valid_date(self):
        yearUp = int(self.order_date.strftime('%Y'))
        currentYear = int(datetime.datetime.now().year)
        if(yearUp<=currentYear):
            difference = yearUp - currentYear
            return difference <2

class Discount(models.Model):
    discount_price = models.FloatField()
    product = models.ManyToManyField(Product)
    
    def is_valid_discount(self):
        return self.discount_price >0