from itertools import product
from django.shortcuts import get_object_or_404, redirect, render
from .models import Cart

from .utils import get_or_create_cart
from products.models import Product
from carts.models import CartProducts

def cart(request):
    cart = get_or_create_cart(request)
    return render(request, 'carts/cart.html', {
        'cart':cart
    })

def add(request):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    quantity = int(request.POST.get('quantity', 1))
    
    #cart.products.add(product, through_defaults={
    #    'quantity': quantity
    #})

    #cart_product = CartProducts.objects.create( cart=cart, 
    #                                            product=product, 
    #                                            quantity=quantity)
    cart_product = CartProducts.objects.create_or_update_quantity(  cart = cart,
                                                                    product = product,
                                                                    quantity = quantity)

    return render(request, 'carts/add.html', {
        'quantity': quantity,
        'cart_product':cart_product,
        'product': product
    })

def remove(request):
    get_object_or_404
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))

    cart.products.remove(product)

    return redirect('carts:cart')