from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from . import views
from products.views import ProductListView


urlpatterns = [
    # 1 = ruta
    # 2 = funcion que se quiere ejecutar
    #path('', views.index, name='index'),
    path('', ProductListView.as_view(), name='index'),
    path('usuarios/login', views.login_view, name='login'),
    path('usuarios/logout', views.logout_view, name='logout'),
    path('usuarios/registro', views.register, name='register'),
    path('admin/', admin.site.urls),
    #producto
    path('productos/', include('products.urls')),
    path('carrito/', include('carts.urls')),
    path('orden/', include('orders.urls')),
    path('direcciones/', include('shipping_addresses.urls')),
    
]

#permite mostrar las imagenes en el template
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
