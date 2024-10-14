from django.db import models 
from restaurant.models import Store, Foods
from users.models import User

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        db_table = 'Customer_customer'
        verbose_name = 'customer'
        verbose_name_plural ='customer'
        ordering = ['-id']

    def __str__(self):
        return self.user.email

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Foods, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    amount = models.FloatField()
    quantity = models.IntegerField()


    class Meta:
        db_table = 'customer_cart'
        verbose_name = 'cart'
        verbose_name_plural ='carts'
        ordering = ['-id']

    def __str__(self):
        return self.customer.user.email
    

class Offer(models.Model):
    code = models.CharField(max_length=50, )
    offer_description = models.TextField()
    offer_amount = models.IntegerField()

    class Meta:
        db_table = 'customer_offer'
        verbose_name = 'offer'
        verbose_name_plural ='offers'
        ordering = ['-id']

    def __str__(self):
        return self.code
    
class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    appartment = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pin_code = models.IntegerField()
    mobile_no = models.IntegerField(default="+91")
    address_type =models.CharField(max_length=50, choices=[('home', 'Home'), ('work', 'Work'), ('other', 'Other'),], default="home")
    
    class Meta:
        db_table = 'customer_address'
        verbose_name = 'address'
        verbose_name_plural ='addresses'
        ordering = ['-id']

    def __str__(self):
        return self.address

class CartBill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item_total = models.DecimalField(max_digits=10, decimal_places=2)
    offer_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    delivery_charge = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'customer_cartbill'
        verbose_name = 'cartbill'
        verbose_name_plural ='cartbills'
        ordering = ['-id']

    def __str__(self):
        return self.customer.user.email

