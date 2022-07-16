from django.db import models

from django.contrib.auth.models import AbstractUser

#AbstractUser
class User(AbstractUser):
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

# Create your models here.
class Customer(User):
    class Meta:
        proxy = True
    
    def get_products(self):
        return()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.TextField()