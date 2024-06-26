from django.shortcuts import redirect,render
from django.views import View
from Product.model.product import Product


class Cart(View):
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_product_by_id(ids)
        print(products)
        return render(request,'cart.html',{'products':products})
