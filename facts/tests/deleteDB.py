from facts.models import Product
from facts.models import NutriFact
from facts.models import NutriTable


Product.objects.all().delete()
NutriFact.objects.all().delete()
NutriTable.objects.all().delete()