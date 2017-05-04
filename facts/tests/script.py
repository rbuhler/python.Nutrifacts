from facts.models import Product
from facts.models import NutriFact
from facts.models import NutriTable


barcode = 7896016601965

products = Product.objects.filter(barcode=barcode)
facts = NutriFact.objects.all()
table = NutriTable.objects.all()

print('\n')
print('Facts : ')

for prod in products:
    print('\n')
    print('Product : ')
    print(prod.name)
    nutriList = prod.nutrifact_set.all
    for nutri in nutriList:
        print('\n')
        print('Serving Size : ')
        print (nutri.servingSize)
