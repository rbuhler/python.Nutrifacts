from facts.models import Product, NutriTable, NutriFact

products = Product.objects.all()
nutritiontable = NutriTable.objects.all()
nutritionfacts = NutriFact.objects.all()
