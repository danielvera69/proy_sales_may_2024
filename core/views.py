from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def home(request):
   data = {
        "title1":"Autor | TeacherCode",
        "title2":"Super Mercado Economico"
   }
   return render(request,'core/home.html',data)

  #  return HttpResponse(f"<h1>{data['title2']}<h1>\
  #                        <h2>Le da la Bienvenida  a su selecta clientela</h2>")
  #  products = ["aceite","coca cola","embutido"]
  #  prods_obj=[{'nombre': producto} for producto in products] # json.dumps()
  #  return JsonResponse({'mensaje2': data,'productos':prods_obj})

 
  #  return HttpResponse(f"<h1>{data['title2']}<h1>\
  #                      <h2>Le da la Bienvenida  a su selecta clientela</h2>")
   
def product_List(request):
    data = {
        "title1": "Productos",
        "title2": "Consulta De Productos"
    }
    # products = Product.objects.all() // data['title1'] == {{title1}}
    # data["products"]=products
    return render(request,"core/products/list.html",data)

def brand_List(request):
    data = {
        "title1": "Marcas",
        "title2": "Consulta De Marcas De Productos"
    }
    return render(request,"core/brands/list.html",data)

def supplier_List(request):
    data = {
        "title1": "Proveedores",
        "title2": "Consulta De proveedores"
    }
    return render(request,"core/suppliers/list.html",data)
  