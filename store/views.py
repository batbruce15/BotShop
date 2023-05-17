from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from store.models import Product, Carte, Order


# Create your views here.


def index(request):
    products = Product.objects.all()  # to recuperate data from database
    return render(request,"store/index.html", context={"products": products})


def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)  # si object existe il le retourn si non il affiche une page 404
    return render(request,"store/details.html",context={"products": product})


def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug = slug)
    cart, _ = Carte.objects.get_or_create(user = user)
    order, created = Order.objects.get_or_create(user = user, ordered = False , product = product)
    if created :
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()
    return redirect(reverse("product", kwargs={"slug":slug}))


def carte(request):
    cart = get_object_or_404(Carte, user = request.user)

    return render(request,"store/carte.html", context={"orders":cart.orders.all()})


def carte_delete(request):
    if carte := request.user.carte:
        carte.delete()
    return redirect("index")