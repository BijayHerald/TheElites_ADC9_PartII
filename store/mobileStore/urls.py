from django.conf.urls import url
from . import views
from django.urls import path
from .views import *
from django.conf import settings 
from django.conf.urls.static import static 


app_name = 'mobile_store'

urlpatterns = [

	path('mobile/', index_page, name='homepage'), #Path of index page or home page
	path('mobile/edit/<int:ID>', update_dataform),			 #Path of update data
	path('mobile/edit/Update/<int:ID>', update_data),		 #Path of edit data
	path('mobile/delete/<int:ID>', delete_data),			 #Path of delete data
	] 

