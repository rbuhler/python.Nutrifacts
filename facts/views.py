from django.shortcuts import render

from facts import DataAccess
from .models import Product
from .models import NutriFact
from .models import NutriTable

# Create your views here.


def index(request):

    return render(request, 'facts/index.html')


def product_list(request):
    all = DataAccess()

    all.all_products()

    products = all.products
    facts = all.facts
    table = all.table.order_by('componentID')
    # products = Product.objects.all()
    # facts = NutriFact.objects.all()
    # table = NutriTable.objects.all().order_by('componentID')

    return render(request, 'facts/product_list.html', {'products': products,
                                                       'facts': facts,
                                                       'table': table})


def product_detail(request, barcode):
    products = Product.objects.filter(barcode=barcode)
    if len(products) > 0:
        for prod in products:
            facts = NutriFact.objects.filter(product=prod.id)
            table = NutriTable.objects.filter(product=prod.id).order_by('componentID')

    return render(request, 'facts/product_detail.html', {'products': products,
                                                         'facts': facts,
                                                         'table': table})
