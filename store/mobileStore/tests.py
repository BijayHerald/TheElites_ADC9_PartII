from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Order, Product, Customer, Discount

# Create your tests here.

class Setup_class(TestCase):


    def setUp(self):
        category1 = Category.objects.create(name="Redmi")
        p1 = Product.objects.create(name="name1", Fullprice= 10, Discountprice=5, image=None )
        c1 = Customer.objects.create(cus_name="Prabesh", cus_address= "Khotang", cus_phone=123)
        d1 = Discount.objects.create(discount_price = 10.00)
        order=Order.objects.create(order_date="2020-1-12",customer=c1,product=p1)


    def test_is_valid_category(self):
        category2 = Category.objects.get(name="Redmi")
        value = category2.is_valid_category()
        self.assertTrue(value, True)


    def test_is_valid_date(self):
        order1 = Order.objects.get(order_date = "2020-1-12")
        value = order1.is_valid_date()
        self.assertTrue(value,True)


    def test_is_valid_Fullamount(self):
        p2 = Product.objects.get(name="name1")
        value=p2.is_valid_Fullamount()
        self.assertEqual(value,10)


    # def test_is_valid_image(self):
    #     p3 = Product.objects.get(name="name1")
    #     value= p3.test_is_valid_image()
    #     salf.assertTrue(value, True)



    def test_is_valid_number(self):
        c2 = Customer.objects.get(cus_name="Prabesh")
        value=c2.is_valid_number()
        self.assertEqual(value,123)




    def test_is_valid_discount(self):
        d1 = Discount.objects.get(discount_price="10.00")
        value=d1.is_valid_discount()
        self.assertTrue(value, True)
