from django.shortcuts import render
from .models import Product
from .models import NutriFact

# Create your views here.


def product_list(request):
    products = Product.objects.all()
    nutriFacts = NutriFact.objects.all()
    return render(request, 'facts/product_list.html', {'products': products,
                                                       'facts': nutriFacts})

