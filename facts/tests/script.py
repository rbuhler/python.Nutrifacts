from facts.models import Product
from facts.models import NutriFact
from facts.models import NutriTable


barcode = 7896016601965
products = Product.objects.filter(barcode=barcode)

print('\n')
print('Size of products : ' + str(len(products)))
print('\n')
print('Facts : ')
for prod in products:
    print('\n')
    print('Product : ' + prod.name)
    facts = NutriFact.objects.filter(product=prod.id)
    table = NutriTable.objects.filter(product=prod.id)
    for nutri in facts:
        print('\n')
        print('Serving Size : ' + str(nutri.servingSize))
    for tab in table:
        print('Component : ' + tab.componentID)

print('End')
