from .cart import Cart

# Create a context processor
def cart(request):
    # Return a dictionary with the 'cart' key and the Cart instance as its value
    return {'cart': Cart(request)}
