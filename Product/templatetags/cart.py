from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(Product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == Product.id:
            return True
    return False


@register.filter(name='cart_quantity')
def cart_quantity(Product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == Product.id:
            return cart.get(id)
    return False

@register.filter(name='price_total')
def price_total(Product,cart):
    return Product.price*cart_quantity(Product,cart)

@register.filter(name='total_cart_price')
def total_cart_price(products,cart):
    sum=0
    for p in products:
        sum +=price_total(p,cart)
    return sum

