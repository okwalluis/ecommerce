from django.shortcuts import render
from django.http import HttpResponse

#Permite responder a una url

def index(request):
    #return HttpResponse('Hola Mundo!')
    return render(request, 'index.html', {
    # context
    })