from facts.models import Product
from facts.models import NutriFact
from facts.models import NutriTable

products = Product.objects.all()
nutritiontable = NutriTable.objects.all()
nutritionfacts = NutriFact.objects.all()