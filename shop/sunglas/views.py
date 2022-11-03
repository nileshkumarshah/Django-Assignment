from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .forms import market, conts
from .models import shoping, product, Categary, Contacts
from django.views import View

# Create your views here.
def about(request):
    """the about functions render to about.html page"""
    return render(request, 'about.html')
    
def glas(request):
    """the glas functions render to glasses.html page"""
    return render(request, 'glasses.html')

def index(request):
    """the index functions render to index.html home page"""
    return render(request, 'index.html')
    
def demo(request):
    """the demo functions render to demo.html page"""
    return render(request, 'demo.html')

# New user contact to admin
def contact(request):
    """the contact method work on request dat get in the input data to the save Contacts tables."""
    if request.method == 'POST':
        shop = conts(request.POST)
        if shop.is_valid():
            name = shop.cleaned_data['name']
            email = shop.cleaned_data['email']
            phone = shop.cleaned_data['phone']
            message = shop.cleaned_data['messages']
            cor = Contacts(name=name, email=email, phone=phone, messages=message)
            cor.save()
            messages.warning(request, 'Contact Send Successfully !!!.')
    else:
        shop = conts()
    return render(request, 'contact.html', {'sho': shop})

def shop(request):
    return render(request, 'shop.html')


# User SingUp form POST data
def regis(request):
    """SingUp page using regis functions in request.POST the forms check the validation data and shopping tables(Create a new Users)"""
    if request.method == 'POST':
        shop = market(request.POST)
        if shop.is_valid():
            name = shop.cleaned_data['name']
            email = shop.cleaned_data['email']
            address = shop.cleaned_data['address']
            phone = shop.cleaned_data['phone']
            password = shop.cleaned_data['password']
            gender = shop.cleaned_data['gender']
            reg = shoping(name=name, email=email, address=address, phone=phone, password=password, gender=gender)
            reg.save()
            messages.warning(request, 'Registration Successfully !!!.')
    else:
        shop = market()
    return render(request, 'register.html', {'sho': shop})

# User login form match database user login
def login(request):
    """The Login user in the check shoping tables match email and password"""
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = shoping.objects.filter(email=email, password=password)
        if user:
            request.session['user'] = email      
            return render(request, 'index.html')              
        else:
            return redirect('login.html')        
    else:
        return render(request, 'login.html')

# User logout
def logout(request):
    """the Logout functions using store the sessions users to delete"""
    try:
        del request.session['user']    
    except TypeError:
     pass
    return render(request, 'index.html')
    

# Get all products and show product
def produ(request):
    """produ function to work Get all the product data in show product pages"""
    prds = product.get_all_products()
    return render(request, 'product.html', {'products': prds})


# Add to cart and remove to cart in POST method
# Total of add cart and show product (ADD TO CART) button
class addtocart(View):
    def post(self, request, id):
        progress = request.POST.get('progress')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(progress)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(progress)
                    else:
                        cart[progress] = quantity-1
                else:
                    cart[progress] = quantity+1
            else:
                cart[progress] = 1
        else:
            cart = {}
            cart[progress] = 1
        request.session['cart'] = cart
        #print("test",request.session['cart'])
        # context = {}
        # context['sessionCart'] = request.session['cart']
        # print("cartsession.",context)
        return render(request, 'cart.html')

    def get(self, request, id):
        categarys = Categary.get_all_categaries()
        categaryID = request.GET.get('categary')
        if categaryID:
            products = product.get_all_products_categary_id(categaryID)
        else:
            products = product.get_all_products()
        data = {}
        data['products'] = products
        data['categarys'] = categarys
        return render(request, 'cart.html', data)


# Upload product (ADD PRODUCT) form in name, price and images (urls)
def Upload_Images(request):
    """Create a new product for using the Upload_Images functions we work in product name, price and images to save in product tables """
    if request.method == 'POST':
        names = request.POST.get('fname')
        price = request.POST.get('price')
        images = request.POST.get('img')
        categarys = Categary.get_all_categaries()
        categary = categarys[0]
        products = product(name=names, categary=categary, price=price, images=images)
        if products:
            products.save()
            return render(request, 'product.html')
    else:
        return render(request, 'product.html')


# Delete product with product id delete method
def Delete_Product(request, id):
    """The show all product to get id and filter in product data match data delete"""
    productId = product.objects.filter(id=id).delete()
    if productId:
        return render(request, 'cart.html')
    return render(request, 'cart.html')

# Update product using product name match and update data

def Update_Product(request):
    """The Update product data to have needs for old product name bases upload data in databases to new upload the product name, price and images."""
    if request.method == 'POST':
        product_name = request.POST.get('pname')
        names = request.POST.get('uname')
        price = request.POST.get('uprice')
        images = request.POST.get('uimg')
        categarys = Categary.get_all_categaries()
        categary = categarys[0]
        productdata = product.objects.filter(name=product_name).update(name=names, categary=categary, price=price, images=images)
        if productdata:
            return render(request, 'product.html')
        else:
            return render(request, 'product.html')
    else:
        return render(request, 'product.html')






