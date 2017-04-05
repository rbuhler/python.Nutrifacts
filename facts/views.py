from django.shortcuts import render
from .models import Product
from .models import NutriFact
from .models import NutriTable

# Create your views here.


def product_list(request):
    products = Product.objects.all()

    for prod in products:
        facts = NutriFact.objects.filter(product_id=prod.id)
        table = NutriTable.objects.filter(product_id=prod.id)

    return render(request, 'facts/product_list.html', {'products': products,
                                                       'facts': facts,
                                                       'table': table})

