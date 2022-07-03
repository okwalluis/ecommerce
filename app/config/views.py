from email import message
import imp
from django.shortcuts import redirect
from django.shortcuts import render

#from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login #genera la sesion
from django.contrib.auth import logout
from django.contrib.auth import authenticate #autentifica el usuario

#Permite responder a una url

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