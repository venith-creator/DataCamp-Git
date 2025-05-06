from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ContactMessage, Offer
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def index(request):
    VENITHfastcars = Product.objects.all()
    return render(request, 'VENITHfastcars/index.html', {'VENITHfastcars': VENITHfastcars})


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'VENITHfastcars/product_detail.html', {'product': product})

def buy(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'VENITHfastcars/buy.html', {'product':product})


def new(request):
    return HttpResponse('New cars')


def about(request):
    return render(request, 'VENITHfastcars/about.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            return render(request, 'VENITHfastcars/contact_success.html', {'name': form.cleaned_data['name']})
    else:
        form = ContactForm()

    return render(request, 'VENITHfastcars/contact.html', {'form': form})


def confirm_purchase(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    print(product)
    return render(request, 'VENITHfastcars/confirm_purchase.html', {'product':product})


@login_required(login_url='login')
def offer_list(request):
    offers = Offer.objects.all()
    return render(request, 'VENITHfastcars/offers.html', {'offers': offers})

def logout_view(request):
    logout(request)
    return redirect('home')