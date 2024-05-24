from django.views import View
from django.shortcuts import redirect
from Product.model.product import Product
from Product.model.orders import Order



class CheckOut(View):
    def post(selfself, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        register = request.session.get('name')
        cart = request.session.get('cart')
        products = Product.get_product_by_id(list(cart.keys()))
        print(register, products)
        return redirect('cart')

        for product in products:
            order = Order(register=register,
                          product=product.id,
                          price=product.price,
                          quantity=cart.get(str(product.id)))
        request.session['cart']={}
        return redirect('cart')
