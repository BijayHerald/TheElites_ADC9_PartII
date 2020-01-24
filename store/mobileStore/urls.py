from django.conf.urls import url
from . import views
from django.urls import path
from .views import *
from django.conf import settings 
from django.conf.urls.static import static 


app_name = 'mobile_store'

urlpatterns = [

	path('mobile/', index_page, name='homepage'), #Path of index page or home page
	path('mobile/form', view_add_product_form),   #Path of add product form
	path('mobile/list', product_list),			   #Path of product list 
	] 

