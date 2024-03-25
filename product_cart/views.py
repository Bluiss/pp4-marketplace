from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, Product
import logging

@login_required
def add_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_product, created = Cart.objects.get_or_create(product=product, user=request.user)
    if not created:
        cart_product.quantity += 1
        cart_product.save()
        messages.success(request, "Product added to cart")
    return redirect("product_cart:cart_detail")



@login_required
def delete_cart(request, product_id):
    cart_product = get_object_or_404(Cart, product_id=product_id, user=request.user)
    if cart_product:
        cart_product.delete()
        messages.success(request, "Product removed from cart")
    else:
        messages.error(request, "Product not found in cart")
    return redirect("product_cart:cart_detail")






@login_required
def cart_detail(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = 0

    for item in cart_items:
        if item.product is not None and item.product.price is not None:
            total_price += item.quantity * item.product.price
        else:
            if item.product:
                logging.warning(f"Product {item.product.name} (ID: {item.product.id}) in cart has no price set.")
            else:
                logging.warning(f"A product in cart (ID: {item.id}) has no associated product.")
            item.delete()

    return render(request, "cart/cart_detail.html", {"cart_items": cart_items, "total_price": total_price})
