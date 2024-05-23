from django.shortcuts import redirect,render
from Product.model.product import Product
from Product.model.categories import Categories
from django.views import View

class Index(View):
    def get(self, request):
        parent_categories = Categories.objects.filter(parent=None)
        categories_with_children = []

        for parent_category in parent_categories:
            category_data = {'parent': parent_category, 'children': parent_category.children.all()}
            categories_with_children.append(category_data)

        products = Product.objects.all()

        category_id = request.GET.get('category')
        if category_id:
            category = Categories.objects.get(id=category_id)
            children_categories = category.children.all()
            products = Product.objects.filter(category__in=[category] + list(children_categories))

        data = {
            'products': products,
            'categories_with_children': categories_with_children,
            'cart': request.session.get('cart', {})
        }

        return render(request, 'index.html', data)

    def post(self,request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart=request.session.get('cart',{})
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity + 1

            else:
                cart[product]=1
        else:
            cart={}
            cart[product] = 1

        request.session['cart']=cart
        print(request.session['cart'])
        return render(request, 'index.html')