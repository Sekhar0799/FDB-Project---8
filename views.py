from django.shortcuts import render , get_object_or_404
from django.http import request , HttpResponse
import json
# Create your views here.

from .models import Product , Customer , ShoppingCart

def home(request):
    products = Product.objects.all()
    return render(request, 'app/home.html', {'products': products})


def product_detail_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = list(range(product.quantity))
    if request.method == 'POST':
        # Get or create the customer
        customer, created = Customer.objects.get_or_create(customer_name='Guest')  # Update with actual customer details

        # Get the selected quantity from the form
        selected_quantity = int(request.POST.get('quantity', 1))

        # Get or create the shopping cart
        shopping_cart, created = ShoppingCart.objects.get_or_create(customer=customer, product=product)

        # Update the quantity or set it to the selected quantity
        shopping_cart.quantity = selected_quantity
        shopping_cart.save()
    return render(request, 'app/product_detail.html', {'product': product , 'quantity_range':context},)



def cart_view(request):
    # Assuming you have a way to identify the current customer, for example, using the session
    customer, created = Customer.objects.get_or_create(customer_name='Guest')

    # Get or create the shopping cart
    cart, created = ShoppingCart.objects.get_or_create(customer=customer)

    # Access related objects directly to get items
    items = cart.product  # Assuming a related name of 'product_set'

    # Calculate total price
    total_price = sum(item.quantity * item.product.price for item in items)

    return render(request, 'cart.html', {'items': items, 'total_price': total_price})