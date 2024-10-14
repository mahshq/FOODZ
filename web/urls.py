from django.urls import path
from web import views

app_name = "web" 

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),

    path("restaurant/<int:id>/", views.restaurant, name="restaurant"),
    path("single_rest/<int:id>/", views.single_rest, name="single_rest"),
    path("add_to_cart/<int:id>/", views.add_to_cart, name="add_to_cart"),
    path("cart_plus/<int:id>/", views.cart_plus, name="cart_plus"),
    path("cart_minus/<int:id>/", views.cart_minus, name="cart_minus"),
    

    path("cart/", views.cart, name="cart"),
    path("add_address/", views.add_address, name="add_address"),
    path("address/", views.address, name="address"),
    path("offers/", views.offers, name="offers"),

    
]
