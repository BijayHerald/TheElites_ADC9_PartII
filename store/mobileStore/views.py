from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.http import HttpResponse
from .forms import *



# View function of getting id
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    return render(request,'mobile/list.html',{
        'products': product
    })





# View function of updating data through update form from updataform.html page through id
def update_dataform(request,ID):
    print(ID)
    list_obj = Product.objects.get(id=ID)
    print(list_obj)
    contex_variable = {
        'product' : list_obj
    }
    return render(request, 'mobile/updateform.html', contex_variable)



# View function of updating data 
def update_data(request,ID):
    print(ID)
    list_obj = Product.objects.get(id=ID)
    print(list_obj)
    list_obj.name = request.POST['product_name']
    list_obj.Fullprice = request.POST['product_fullprice']
    list_obj.Discountprice = request.POST['product_discount_price']
    list_obj.image = request.POST['image']
    list_obj.save()
    return HttpResponse("Data Updated successfully")


# View function of Deleting data 
def delete_data(request,ID):
        print(ID)
        list_obj = Product.objects.get(id=ID)
        list_obj.delete()
        return HttpResponse("Data Deleted successfully")




















