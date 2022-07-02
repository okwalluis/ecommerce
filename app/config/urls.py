from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    # 1 = ruta
    # 2 = funcion que se quiere ejecutar
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
