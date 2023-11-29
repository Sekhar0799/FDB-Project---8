from django.contrib import admin

# Register your models here.
from .models import Vendor, Customer, Admin, Category, SubCategory, Product, Order, Transaction, Review, Advertisement, PaymentGateway, Wishlist, PaymentMethod, ShippingAddress,ShoppingCart , BillingAddress, Return, Refund, AdSlot, DiscountPromotion

admin.site.register(Vendor)
admin.site.register(Customer)
admin.site.register(Admin)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Transaction)
admin.site.register(Review)
admin.site.register(Advertisement)
admin.site.register(PaymentGateway)
admin.site.register(ShoppingCart)
admin.site.register(Wishlist)
admin.site.register(PaymentMethod)
admin.site.register(ShippingAddress)
admin.site.register(BillingAddress)
admin.site.register(Return)
admin.site.register(Refund)
admin.site.register(AdSlot)
admin.site.register(DiscountPromotion)
