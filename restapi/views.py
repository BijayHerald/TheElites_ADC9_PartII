# from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from mobileStore.models import Product
from django.core.paginator import Paginator



@csrf_exempt
def view_get_post_product(request):
    print("what is the request =>", request.method)
    if request.method == "GET":
        products = Product.objects.all()
        print("Query objects =>", products)
        list_of_products = list(products.values("name","Fullprice","Discountprice"))
        print("list of Product objects =>", list_of_products)
        dictionary_name = {
            "products" : list_of_products
        }


        return JsonResponse(dictionary_name)
    elif request.method == "POST":
        print("Request body content =>", request.body)
        print("Request body type =>", type(request.body))
        python_dictionary_object = json.loads(request.body)
        print("Python dictionary contents=>",python_dictionary_object)
        print("Python dictionary type=>",type(python_dictionary_object))
        print(python_dictionary_object['name'])
        print(python_dictionary_object['Fullprice'])
        print(python_dictionary_object['Discountprice'])
        Product.objects.create(name=python_dictionary_object['name'],Fullprice=python_dictionary_object['Fullprice'], Discountprice=python_dictionary_object['Discountprice'])
        return JsonResponse({
            "message":"Successfully posted!!"
        })
    






    else:
        return HttpResponse("Other HTTP verbs testing")







@csrf_exempt
def view_getByID_updateByID_deleteByID(request,ID):
    print("What's the request =>",request.method)
    if request.method == "GET":
        product = Product.objects.get(id = ID)
        print(type(product.name))
        return JsonResponse({
            "id":product.id,
            "name":product.name,
            "Fullprice":product.Fullprice,
            "Discountprice":product.Discountprice

        })


    else:
        return JsonResponse({
        "message":" Other htpp verbs Testing"
        })




@csrf_exempt
def api_delete_data(request, ID):
    print("What's the request =>",request.method)
    product = Product.objects.get(id = ID)
    print(type(product.name))
    if request.method == "DELETE":
        product.delete()
        return JsonResponse({"Message" : "Delete Completed"})

    else:
        return JsonResponse({"id":product.id,
            "name":product.name,
            "Fullprice":product.Fullprice,
            "Discountprice":product.Discountprice
            })





@csrf_exempt
def api_update_data(request, ID):
    product = Product.objects.get(id = ID)
    if request.method == "PUT":
        decoded_data = request.body.decode('utf-8')
        product_data = json.loads(decoded_data)
        product.name = product_data['name']
        product.Fullprice = product_data['Fullprice']
        product.Discountprice = product_data['Discountprice']
        
        product.save()

        return JsonResponse({"Message" : "Update Completed"})

    else:
        return JsonResponse({"id":Product.id,
            "name":Product.name,
            "Fullprice":Product.Fullprice,
            "Discountprice":Product.Discountprice
            })

            



@csrf_exempt
def api_product_pagination(request, PAGENO):
    SIZE = 3
    skip = SIZE * (PAGENO-1)
    product = Product.objects.all() [skip:PAGENO*SIZE]
    dict = {
        "product": list(product.values("name","Fullprice","Discountprice"))
    }
    return JsonResponse(dict)















