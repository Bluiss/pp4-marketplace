from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart 
from .models import Product

# Create your views here.
# Add cart view
@login_required
def add_cart(request, product_id):
    cart_product = get_object_or_404(Product, id=product_id)

    if cart_product:
        cart_product.quantity += 1
        cart_product.save()
        messages.success(request, "Product added to cart")
    else:
        cart_product = Product.objects.create(product=cart_product)
        cart_product.save()
        messages.success(request, "Product added to cart")

    return redirect("cart:cart_detail")


def delete_cart(request, product_id):
    cart_product = get_object_or_404(Product, id=product_id)

    if cart_product:
        cart_product.quantity -= 1
        cart_product.save()
        messages.success(request, "Product removed from cart")
    
    return redirect("cart:cart_detail")


def cart_detail(request):
    cart = Cart.objects.filter(user=request.user)
    total = 0
    for product in cart:
        total += product.quantity * product.product.price

    return render(request, "cart/cart_detail.html", {"cart": cart, "total": total})

    







# delete cart view
# cart detail view




