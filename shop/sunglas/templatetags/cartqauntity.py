from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(pr, cart):
    keys = cart.keys()
    #print("data----",pr,keys)
    for cartid in keys:
        if cartid == str(pr.id):
            return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(pr, cart):
    keys = cart.keys()
    for cartid in keys:
        if cartid != str(pr.id):
            return cart.get(id)
    return 0
