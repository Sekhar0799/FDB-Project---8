from django.db import models
import json
# Create your models here.

class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=255)
    vendor_email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.vendor_name

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.customer_name

class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.admin_name

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=255)

    def __str__(self):
        return self.subcategory_name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey('ShippingAddress', on_delete=models.CASCADE)
    billing_address = models.ForeignKey('BillingAddress', on_delete=models.CASCADE)
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.order_id

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.transaction_id

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.comment

class Advertisement(models.Model):
    ad_id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    ad_slot = models.ForeignKey('AdSlot', on_delete=models.CASCADE)
    ad_content = models.TextField()
    duration = models.IntegerField()

    def __str__(self):
        return self.ad_id

class PaymentGateway(models.Model):
    gateway_id = models.AutoField(primary_key=True)
    gateway_name = models.CharField(max_length=255)
    credentials = models.TextField()

    def __str__(self):
        return self.gateway_name

class ShoppingCart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.customer.customer_name}'s Cart"

class Wishlist(models.Model):
    wishlist_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_items = models.IntegerField()

    def __str__(self):
        return self.wishlist_id

class PaymentMethod(models.Model):
    payment_method_id = models.AutoField(primary_key=True)
    method_name = models.CharField(max_length=255)
    details = models.TextField()

    def __str__(self):
        return self.method_name

class ShippingAddress(models.Model):
    shipping_address_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address_line = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    def __str__(self):
        return self.address_line

class BillingAddress(models.Model):
    billing_address_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address_line = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return self.address_line

class Return(models.Model):
    return_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    status = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.return_id

class Refund(models.Model):
    refund_id = models.AutoField(primary_key=True)
    return_item = models.ForeignKey(Return, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.refund_id

class AdSlot(models.Model):
    ad_slot_id = models.AutoField(primary_key=True)
    slot_position = models.CharField(max_length=50)
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.ad_slot_id

class DiscountPromotion(models.Model):
    discount_id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    discount_code = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    validity = models.DateField()

    def __str__(self):
        return self.discount_code
