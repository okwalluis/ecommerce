from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from products.models import Product

class ProductListView(ListView):
    template_name= 'index.html'
    queryset= Product.objects.all().order_by('-id')

    #sobreescribir metodo
    #que se encarga de pasar el contexto de la clase al template
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       
       context['message'] = 'Listado de productos'
    #imprimir en consola los datos del context
       #print(context)
       return context

#la clase se encarga de recuperar un registro mediante el id
class ProductDetailView(DetailView): #id ->pk
    model = Product
    template_name = 'products/product.html'

    #def get_context_data(self, **kwargs):
    #  context = super().get_context_data(**kwargs)
    #  #imprimir en consola los datos del context
    #  print(context) 
    #  return context

