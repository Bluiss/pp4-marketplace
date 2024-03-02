class Cart():
    def __init__(self, request):
        self.session = request.session 

        # get current session key 
        cart = self.session.get('session_key')

        # if this user has no session, create one
        if cart is None:
            cart = self.session['session_key'] = {}

        # make cart available on all pages
        self.cart = cart


    def add(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': product.price}

        self.session = True