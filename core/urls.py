from django.urls import path
from core import views
 
app_name='core' # define un espacio de nombre para la aplicacion
urlpatterns = [
   path('product_list/', views.product_List,name='product_list'),
   path('brand_list/', views.brand_List,name='brand_list'),
   path('supplier_list/', views.supplier_List,name='supplier_list'),
]