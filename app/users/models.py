from django.db import models

from django.contrib.auth.models import AbstractUser

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

# Create your models here.
class Customer(User):
    class Meta:
        proxy = True
    
    def get_products(self):
        return()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.TextField()