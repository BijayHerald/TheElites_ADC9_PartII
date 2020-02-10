from django.urls import path
from .views import *


urlpatterns = [
    path('products/',view_get_post_product),
    path('products/<int:ID>',view_getByID_updateByID_deleteByID),
    path('products/delete/<int:ID>', api_delete_data),
    path('products/update/<int:ID>', api_update_data),
    path('products/page/<int:PAGENO>', api_product_pagination)

]