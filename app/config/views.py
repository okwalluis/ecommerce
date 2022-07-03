from email import message
import email
import imp
from django.shortcuts import redirect
from django.shortcuts import render

#from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login #genera la sesion
from django.contrib.auth import logout
from django.contrib.auth import authenticate

from config.forms import RegisterForm #autentifica el usuario

#Permite responder a una url

from .forms import RegisterForm
from django.contrib.auth.models import User

def index(request):
    #return HttpResponse('Hola Mundo!')
    return render(request, 'index.html', {
    # context= diccionario
        'title':'Productos',
        'products':[
            {'title':'playera','price':5,'stock':True}, #producto
            {'title':'Camisa','price':7,'stock':True},
            {'title':'Mochila','price':20,'stock':False},
        ]
    })

def login_view(request):
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
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username') #diccionario
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = User.objects.create_user(username,email,password)

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