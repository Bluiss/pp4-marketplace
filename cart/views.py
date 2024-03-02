from django.shortcuts import render, get_object_or_404
from .cart import Cart
from product.models import Product
from django.http import JsonResponse

def cart_summary(request):
    return render(request, "cart_summary.html", {})

def cart_add(request):
    # get cart
    cart = Cart(request)
    
    # test post
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        if product_id is None:
            return JsonResponse({'error': 'No product_id in POST data'}, status=400)
        product_id = int(product_id)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)

        response = JsonResponse({'Product Name': product.title})  # change 'name' to 'title'
        return response

def cart_delete(request):
    pass

def cart_update(request):
    pass
