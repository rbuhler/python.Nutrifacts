from itertools import chain

from facts.models import Product
from facts.models import NutriFact
# from facts.models import NutriTable

barcodeA = 7896016601965
barcodeB = 7891000451304

productA = Product.objects.filter(barcode=barcodeA)
productB = Product.objects.filter(barcode=barcodeB)
productC = list(chain(productA, productB))

factsC = []
i = 0
print('\n')
for prod in productC:
    factsC.append(NutriFact.objects.filter(product=prod.id))
    print('Fact C created ...[' + str(i) + ']')
    i = i + 1

print('\n')
print('Size of productC : ' + str(len(productC)))
print('Size of factC : ' + str(len(factsC)))
i = 0
line = []
for prod in productC:
    print('\n')
    print('Product : ' + prod.name)
    print('Facts   : ')
    servingSize = factsC[i].values()[0]['servingSize']
    servingUM = factsC[i].values()[0]['servingUM']
    servingQuantity = factsC[i].values()[0]['servingQuantity']
    servingQtdUm = factsC[i].values()[0]['servingQtdUm']
    footNote = factsC[i].values()[0]['footNote']
    i = i + 1

print('\n')
print('End')
