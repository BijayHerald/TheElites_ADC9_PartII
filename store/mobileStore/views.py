from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.http import HttpResponse
from .forms import *
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# View function of index page
def index_page(request):
    return render(request, 'mobile/index.html')

# View function of adding product
def view_add_product_form(request):
    return render(request,'mobile/add_product.html')


# View function of product listing
def product_list(request):
    categories = Product.objects.all()
    return render(request,'mobile/list.html',{
        'products': categories
    })

# View function of searching data
def product_list_search(request):
    products = Product.objects.filter(name=request.GET['productname'])
    print(products)
# Returning list form of saved data 
    return render(request,'mobile/list.html',{
        'products': products
    })

# View function of getting id
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    return render(request,'mobile/list.html',{
        'products': product
    })





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





































