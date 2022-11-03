from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

# Create your models here.
"""choice the gender using SingUp page in male or femail using the shopping models class"""
GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female')
)

# Registration form using shoping class
class shoping(models.Model):
    """SingUp model class using the fields"""
    name = models.CharField(max_length=90)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=120) 
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=50)
    gender =models.IntegerField(choices=GENDER_CHOICES)

#Contacts user message
class Contacts(models.Model):
    """Contacts as models class using user any send messages"""
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    messages = models.CharField(max_length=150)

# Categary of original and local product
class Categary(models.Model):
    """the categary class models using in product brand types at shopping"""
    name = models.CharField(max_length=30)
    @staticmethod
    def get_all_categaries():
        return Categary.objects.all()

# glasses product
class product(models.Model):
    """the product models class add to the ForeignKey (categary class models admin side set the product brands)
    and product name, price and images uploaded"""
    name = models.CharField(max_length=100)
    categary = models.ForeignKey(Categary, on_delete=models.CASCADE, default=1)
    price = models.IntegerField(null=True)
    images = models.ImageField(upload_to="images/", max_length=100)

    @staticmethod
    def get_all_products():
        """the model based get all product data and call the only functions name"""
        return product.objects.all()

    @staticmethod
    def filter_id_products():
        """the model based filter data to check match the id in product data and call the only functions name"""
        return product.objects.filter(id=id)

    @staticmethod
    def get_all_products_categary_id(categary_id):
        """the model based filter data to check match the categary_id in product data and call the only functions name"""
        if categary_id:
            return product.objects.filter(categary=categary_id)
        else:
            return product.get_all_products()

# Add to cart
class Cart(models.Model):
    """Add to cart in Cart models class using"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.FloatField(null=True)
    ordered = models.BooleanField(null=True)
    
    def __str__(self):
        return str(self.user.username)+" " + str(self.total_price)

# Check cart items
class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    price = models.FloatField(null=True)
    quantity = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return str(self.user.username)+" " + str(self.product.name)

# signals using check cart quantity add price and add total price

@receiver(post_save, sender=CartItems)
def my_callback(sender, **kwargs):
    """signals using check cart quantity add price and add total price"""
    cart_items = kwargs['instance']
    price_of_product = product.objects.get(id=cart_items.product.id)
    cart_items.price = cart_items.quantity * float(price_of_product.price)
    # total_cart_items = CartItems.objects.filter(user=cart_items.user)
    cart = Cart.objects.get(id=cart_items.cart.id)
    cart.total_price = cart_items.price
    cart.save()