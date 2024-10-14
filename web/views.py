from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from users.models import User
from customer.models import Customer, Cart, Offer
from restaurant.models import StoreCategory, Store, Slider, Foods, Food_Category



@login_required(login_url='/login/')
def index(request):
    store_categories = StoreCategory.objects.all()
    stores = Store.objects.all()
    slider = Slider.objects.all()
    context = {
        'store_categories': store_categories,
        'stores': stores,
        'slider': slider,
    }
    return render(request, 'web/index.html', context=context)


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('web:index'))
        else:
            context = {
                'error':True,
                'message':'invalid Email or password'
            }
            return render(request, 'web/login.html', context=context)

    else:
        return render(request, 'web/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            context = {
                'error':True,
                'message':'Email already exists'
            }
            return render(request, 'web/register.html', context=context)

        else:

            user = User.objects.create_user(
                first_name=first_name, 
                last_name=last_name, 
                email=email, 
                password=password,
                is_customer = True,
            )
            user.save()
            customer = Customer.objects.create(
                user=user,  
            )
            customer.save()
            return HttpResponseRedirect(reverse('web:login'))
    else:   
        return render(request, 'web/register.html')
    
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('web:login'))

@login_required(login_url='/login/')
def restaurant(request, id):
    store_categories = StoreCategory.objects.all()
    stores = Store.objects.all()

    selected_category = StoreCategory.objects.get(id=id)

    stores = stores.filter(category=selected_category)

    context = {
        'store_categories': store_categories,
        'stores': stores,
    }
    return render(request, 'web/restaurant.html', context=context)


@login_required(login_url='/login/')
def single_rest(request, id):
    user = request.user
    customer = Customer.objects.get(user=user)
    store = Store.objects.get(id=id)
    food_category = Food_Category.objects.filter(store=store)
    foods = Foods.objects.filter(store=store, food_category__in=food_category)
    carts = Cart.objects.filter(store=store, customer=customer)


    cart_quantities = {cart.product: cart.quantity for cart in carts}
    prod_with_qty = [(food, cart_quantities.get(food, 0)) for food in foods]

    context = {
        'store': store,
        'foods': foods,
        'customer': customer,
        'carts': carts,
        'food_category': food_category,
        'prod_with_qty': prod_with_qty,
    }
    return render(request, 'web/single_rest.html', context=context)


@login_required(login_url='/login/')
def add_to_cart(request, id):
    customer = Customer.objects.get(user=request.user)
    product = Foods.objects.get(id=id)
    cart_items = Cart.objects.filter(customer=customer)

    if cart_items.exists():
        currrent_store = cart_items.first().store
        if product.store != currrent_store:
            cart_items.delete()

    cart = Cart.objects.create(
        product= product,
        customer= customer,
        quantity=1,
        amount=product.amount,
        store=product.store,
    )
    cart.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/login/')
def cart_plus(request, id):
    customer = Customer.objects.get(user=request.user)
    product = Foods.objects.get(id=id)
    cart = Cart.objects.get(product=product, customer=customer)
    cart.quantity += 1
    cart.amount += product.amount
    cart.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/login/')
def cart_minus(request, id):
    customer = Customer.objects.get(user=request.user)
    product = Foods.objects.get(id=id)
    cart = Cart.objects.get(product=product, customer=customer)
    cart.quantity -= 1
    cart.amount -= product.amount
    if cart.quantity == 0:
        cart.delete()
    else:
        cart.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




@login_required(login_url='/login/')
def cart(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    carts = Cart.objects.filter(customer=customer)

    
    
    store = None
    if carts.exists():
        store = carts.first().store
    else:
        store = None


    context = {
        'customer': customer,
        'carts': carts,
        'store': store,
        
    }
        

    return render(request, 'web/cart.html', context=context)


@login_required(login_url='/login/')
def offers(request):
    offers = Offer.objects.all()
    item_total = Cart.objects.all()


    context = {
        'offers': offers,
        'item_total': item_total,
    }
    return render(request, 'web/offers.html', context = context)

def add_address(request):
    return render(request, 'web/add_address.html')

def address(request):
    return render(request, 'web/address.html')