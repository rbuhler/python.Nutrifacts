from facts.models import Product
from facts.models import NutriFact
from facts.models import NutriTable

print('Start >>')

if Product.objects.all().delete():
    print('Products dropped ...')
else:
    print('Products NOT dropped ...')

if NutriFact.objects.all().delete():
    print('Nutrifact dropped ...')
else:
    print('Nutrifact NOT dropped ...')

if NutriTable.objects.all().delete():
    print('Nutritable dropped ...')
else:
    print('NutriTable NOT dropped ...')

print('<< End')
