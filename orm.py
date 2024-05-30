from datetime import date,datetime
from decimal import Decimal,ROUND_HALF_UP
import random
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils import timezone
import os
import django
from django.db.models import F,Q
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum, Avg, Max, Min, Count
from django.db.models.functions import Substr
from argparse import Namespace
# Establece la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proy_sales.settings')
# Inicializa Django
django.setup()
from django.contrib.auth.models import User
from core.models import Brand, Supplier, Product, Category, Customer, PaymentMethod, Invoice, InvoiceDetail

def probar_orm():
  def create_user(create=False):  
    if create:  # Comprueba si create es True
        User.objects.create_user(  
            username='acabrera',  
            password='acfg1234',  
            email='abd@example.com'  
        )
        users = User.objects.all()  # Recupera todos los usuarios de la base de datos y los almacena en la variable users

        print("Listado de Usuarios")
        print(users)
      
  # create_user(True)
   
  def script_brands(create=False):
      if create:
        user= User.objects.get(username='dverap')
        # brand1 = Brand.objects.create(description="Nike", user=user)
        # brand2 = Brand.objects.create(description="Arroz Flor", user=user,state=False)
        # brand3 = Brand.objects.create(description="Atun Real", user=user)
        # brand4 = Brand.objects.create(description="Azucar Valdez", user=user)
        brand5 = Brand.objects.create(description="Nest cafe", user=user)
      print("Listado de las marcas")
      brands= Brand.objects.all()
      print(brands)
      brands= Brand.active_brands.all()
      for brand in brands: print(brand,brand.state) 
  # script_brands(True)
    
  def scripts_category(create=False):
      if create:
        Category.objects.filter(description__in=('electrodomesticos','Atun')).delete()
        user= User.objects.get(id=1)
        cat = Category(description='electrodomesticos',user=user)
        #cat.state=False
        cat.save()
        Category(description='Atun',user=user).save()
      print("Listado de Categorias")
      print(Category.objects.all())
  # scripts_category(True)
    
  def scripts_payment_Method(create=False):
      if create:
        user= User.objects.get(pk=1)
        PaymentMethod.objects.bulk_create([ 
          PaymentMethod(description="Contado",user=user), 
          PaymentMethod(description="Credito",user=user), 
          PaymentMethod(description="Tarjeta",user=user) 
        ]) 
      print("Listado de los Metodos de Pagos")
      print(PaymentMethod.objects.all())
  # scripts_payment_Method(True)   
  def scripts_customer(create=False):
      if create:
        user= User.objects.get(pk=1)
        Customer.objects.bulk_create([ 
          Customer(dni='0914192182',first_name='Daniel',last_name='Vera',address='Milagro',gender='M',date_of_birth=date(1970, 5, 10),user=user), 
          Customer(dni='0914192184',first_name='Miguel',last_name='Berrones',address='9 de Octubre',gender='M',date_of_birth=date(2017, 10, 10),user=user), 
          Customer(dni='0914192185',first_name='Yady',last_name='Bohorquez',address='Pedro Carbo',gender='F',date_of_birth=date(1975, 7, 10),user=user) 
        ]) 
      
      print("Listado de los Clientes")
      customers= Customer.objects.values('id','dni','first_name','last_name')
      customers2= Customer.objects.values_list('id','dni','first_name','last_name')
      print("values list")
      print(customers)
      print("values")
      print(customers2)
      print(list(customers))
      print(list(customers2))
  # scripts_customer(True) 
  def script_queryset():
       Product.objects.filter(id=13).update(state=False)
       product_all = Product.objects.all()
       product_values = Product.objects.values('id','description','price','stock','state')
       product_list = Product.objects.values_list('id','description','price','stock','state')
       product_filter = Product.objects.filter(state=True)
       product_manager = Product.active_products.all() 
       product_exclude = Product.active_products.exclude(price = 200)
       product_exclude = Product.active_products.all().exclude(price = 200)
       product_distinct = Product.objects.values('preci').distinct()
       print("Listado de objetos de Productos: all")
       print(product_all)
       print("Listado de objetos de Productos: values")
       print(product_values)
       print("Listado de objetos de Productos values_list")
       print(product_list)
       print("Listado de objetos de Productos list")
       prods_list = list(product_list)
       prods_id = [prod[2] for prod in prods_list]
       print(prods_list)
       print(prods_id,max(prods_id),sum(prods_id),random.choice(prods_id))
       print("Listado de objetos de Productos: filter")
       print(product_filter)
       print("Listado de objetos de Productos: manager")
       print(product_manager)
       print("Listado de objetos de Productos: exclude")
       print(product_exclude)
  script_queryset()
  
  def script_get():
       print("Objeto Producto")
       try:
         product1 = Product.active_products.get(pk=3)
         print(product1)
       except ObjectDoesNotExist:
         print("El producto con el ID 3 no existe.")  
       try:  
         product2 = get_object_or_404(Product, pk=4)
         print(product2.id,product2.description)
       except Http404 as e:
         print("¡El producto con el ID 4 no existe!")
     