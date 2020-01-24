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
	path('mobile/save', product_image_view, name = 'image_upload'),   #Path of view image option
	path('mobile/search/',product_list_search),			 	 #Path of search
	path("mobile/loginfirst", not_logged_in_condition)		 #Path of login first condition
] 

