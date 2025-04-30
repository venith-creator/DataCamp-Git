from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# /VENITHfastcars -> index
# uniform resource locator

def index(request):
    VENITHfastcars = Product.objects.all()
    return render(request, 'index.html', {'VENITHfastcars': VENITHfastcars})


def new(request):
    return HttpResponse('New cars')


# Create your views here.
