from django.shortcuts import render
from .models import Product
from .models import NutriFact
from .models import NutriTable

# Create your views here.


def product_list(request):
    products = Product.objects.all()
    facts = NutriFact.objects.all()
    table = NutriTable.objects.all()

    return render(request, 'facts/product_list.html', {'products': products,
                                                       'facts': facts,
                                                       'table': table})


def product_detail(request, barcode):
    # bcode = 7896016601965
    product = Product.objects.filter(barcode=barcode).values()
    facts = NutriFact.objects.all()
    table = NutriTable.objects.all()

    return render(request, 'facts/product_detail.html', {'product': product,
                                                         'facts': facts,
                                                         'table': table})
