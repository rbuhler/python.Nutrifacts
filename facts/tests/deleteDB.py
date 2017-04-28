from facts.models import Product
from facts.models import NutriFact
from facts.models import NutriTable

print('\n'+'Start >>')

if Product.objects.all().delete():
    print('\n'+'Products dropped ...')
else:
    print('\n'+'Products NOT dropped ...')

if NutriFact.objects.all().delete():
    print('\n'+'Nutrifact dropped ...')
else:
    print('\n'+'Nutrifact NOT dropped ...')

if NutriTable.objects.all().delete():
    print('\n'+'Nutritable dropped ...')
else:
    print('\n'+'NutriTable NOT dropped ...')

print('\n'+'<< End')
