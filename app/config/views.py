from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import login #genera la sesion
from django.contrib.auth import logout
from django.contrib.auth import authenticate

#from django.http import HttpResponse

from config.forms import RegisterForm #autentifica el usuario
#Permite responder a una url
from .forms import RegisterForm
#from django.contrib.auth.models import User
from users.models import User

from products.models import Product



def index(request):

    products = Product.objects.all().order_by('-id')

    #return HttpResponse('Hola Mundo!')
    return render(request, 'index.html', {
    # context= diccionario
        'message':'Listado de productos',
        'title':'Productos',
        'products': products
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
        
    #print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username') # diccionario
        password = request.POST.get('password')
        #imprimir en consola 
        #print(username)
        #print(password)
        user = authenticate(username=username, password=password) #en caso que no encuentre retorna None
        if user:
            login(request,user)
            messages.success(request, "Bienvenido {}". format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no válidos')

    return render(request, 'users/login.html',{

    })

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        
        #username = form.cleaned_data.get('username') #diccionario
        #email = form.cleaned_data.get('email')
        #password = form.cleaned_data.get('password')

        #user = User.objects.create_user(username,email,password)
        user = form.save()

        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')
        #print(username)
        #print(email)
        #print(password)
    return render(request, 'users/register.html', {
        'form':form
    })