from facts.models import NutriFact
from facts.models import NutriTable
from facts.models import Product

Product.objects.all().delete()
NutriFact.objects.all().delete()
NutriTable.objects.all().delete()