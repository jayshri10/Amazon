from django.views import View
from django.shortcuts import redirect
from Product.model import register
from Product.model.product import Product
from Product.model.orders import Order
from Product.templatetags import cart


class CheckOut(View):
    def post(selfself, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        register = request.session.get('register')
        cart = request.session.get('cart')
        products = Product.get_product_by_id(list(cart.keys()))
        print(address, phone, register, cart, products)
        return redirect('cart')

        for product in Product:
            order = Order(register=register,product=product.id,price=product.price,quantity=cart.get())
        return redirect('cart')
