from django.db import models

from django.contrib.auth.models import AbstractUser

from orders.common import OrderStatus

#AbstractUser
class User(AbstractUser):
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    @property
    def shipping_address(self):
        #shippingaddress_set hace uso de la relacion entre direcciones y usuarios
        #y le agrega el sufijo set
        return self.shippingaddress_set.filter(default=True).first()

    def has_shipping_address(self):
        return self.shipping_address is not None

    def orders_completed(self):
        return self.order_set.filter(status=OrderStatus.COMPLETED).order_by('-id')

    def has_shipping_addreses(self):
        return self.shippingaddress_set.exists()

    @property
    def addresses(self):
        return self.shippingaddress_set.all()

# Create your models here.
class Customer(User):
    class Meta:
        proxy = True
    
    def get_products(self):
        return()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.TextField()