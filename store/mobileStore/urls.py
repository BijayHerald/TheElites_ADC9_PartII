from django.conf.urls import url
from . import views
from django.urls import path
from .views import *
from django.conf import settings 
from django.conf.urls.static import static 


app_name = 'mobile_store'

urlpatterns = [

	path('mobile/', index_page, name='homepage'), #Path of index page or home page
	path('mobile/signup', view_signup_user),				 #Path of signup 
	path('mobile/login', view_login_user),					 #Path of login
	path('mobile/success', view_login_user),				 #Path of login success
	path("mobile/logout", logout_request),					 #Path of logout
	] 

