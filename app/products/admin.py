import imp
from django.contrib import admin

from .models import Product

#se debe registrar el modelo para que el adimnistrador
#pueda gestionar las informaciones.

class ProductAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'price', 'image')
    list_display = ('__str__', 'slug', 'created_at')

admin.site.register(Product, ProductAdmin)