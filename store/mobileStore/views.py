from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.http import HttpResponse
from .forms import *
from django.core.files.storage import FileSystemStorage


# View function of index page
def index_page(request):
    return render(request, 'mobile/index.html')

# View function of adding product
def view_add_product_form(request):
    return render(request,'mobile/add_product.html')



# View function of inserting image
def product_image_view(request): 
  
    if request.method == 'POST': 

        get_img = request.FILES['image']
        fs = FileSystemStorage()
        image = fs.save(get_img.name, get_img)


        form = Product(name = request.POST['product_name'], Fullprice = request.POST['product_fullprice'],image =get_img , Discountprice = request.POST['product_discount_price'],) 
        form.save() 
    return HttpResponse("records saved.")   #showing record saved result
    
  
def success(request): 
    return HttpResponse('successfully uploaded')    #showing record successfully uploaded result






















