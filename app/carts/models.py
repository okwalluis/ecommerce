import uuid
import decimal

from django.db import models
from users.models import User
from products.models import Product
from orders.common import OrderStatus
from django.db.models.signals import pre_save, m2m_changed, post_save

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    # se crear primero las tablas, luego se crea la relacion
    #products = models.ManyToManyField(Product)
    products = models.ManyToManyField(Product, through='CartProducts')
    subtotal = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    total = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    FEE = 0.05 #5% de utilidad

    def __str__(self):
        return self.cart_id
    
    def update_totals(self):
        self.update_subtotal()
        self.update_total()
        #order = self.order_set.first()
        #if order:
        #    order.update_total()
        if self.order:
            self.order.update_total()

    def update_subtotal(self):
        self.subtotal = sum([
            cp.quantity * cp.product.price for cp in self.products_related()
            ])
        self.save()

    def update_total(self):
        self.total = self.subtotal + (self.subtotal * decimal.Decimal(Cart.FEE))
        self.save()

    #obtenemos todos los objetos cartproducts en una consulta.
    def products_related(self):
        return self.cartproducts_set.select_related('product')

    @property
    def order(self):
        return self.order_set.filter(status=OrderStatus.CREATED).first()

class CartProductsManager(models.Manager):
    def create_or_update_quantity(self, cart, product, quantity=1):
        object, created = self.get_or_create(cart=cart, product=product)
        
        if not created:
            quantity = object.quantity + quantity
        
        object.update_quantity(quantity)
        return object

class CartProducts(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CartProductsManager()

    def update_quantity(self, quantity=1):
        self.quantity = quantity
        self.save()

def set_cart_id(sender, instance, *args, **kwargs):
    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())

#callback
def update_totals(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        instance.update_totals()

def post_save_update_totals(sender, instance, *args, **kwargs):
    instance.cart.update_totals()

pre_save.connect(set_cart_id, sender=Cart)
post_save.connect(post_save_update_totals, sender=CartProducts)
m2m_changed.connect(update_totals, sender=Cart.products.through)