from itertools import product
from django.shortcuts import get_object_or_404, redirect, render
from .models import Cart

from .utils import get_or_create_cart
from products.models import Product

def cart(request):
    cart = get_or_create_cart(request)

#    user = request.user if request.user.is_authenticated else None
#    cart_id = request.session.get('cart_id') #None
#    cart = Cart.objects.filter(cart_id=cart_id).first() #()None
#    if cart is None:
#        cart = Cart.objects.create(user=user)
#
#    if user and cart.user is None:
#        cart.user = user
#        cart.save()
#
#    request.session['cart_id'] = cart.cart_id
    return render(request, 'carts/cart.html', {
        'cart':cart
    })

def add(request):
    cart = get_or_create_cart(request)
#    user = request.user if request.user.is_authenticated else None
#    cart_id = request.session.get('cart_id')
#    if cart_id:
#        cart = Cart.objects.get(pk=request.session.get('cart_id'))
#    else:
#        cart = Cart.objects.create(user=user)

#    product = Product.objects.get(pk=request.POST.get('product_id'))
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    #agregar un producto a la lista
    cart.products.add(product)

    return render(request, 'carts/add.html', {
        'product':product
    })

def remove(request):
    get_object_or_404
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))

    cart.products.remove(product)

    return redirect('carts:cart')