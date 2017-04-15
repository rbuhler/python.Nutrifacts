from facts.models import NutriFact
from facts.models import NutriTable
from facts.models import Product
# PRODUCT 1
Product.objects.create(id           = 1,
                       name         = "LEITE DUCOCO TRADICIONAL",
                       manufacturer = "DUCOCO",
                       barcode      = 7896016601965)

NutriFact.objects.create(product_id      = Product.objects.get(id=1),
                         servingSize     = 15,
                         servingUM       = "ML",
                         servingQuantity = 200,
                         servingQtdUm     = "ML",
                         footNote        = "FootNote - footNote")

NutriTable.objects.create( product_id    = Product.objects.get(id=1),
                           componentID   = "VALOR ENERGETICO",
                           componentQuantity = 25,
                           componentUM       = "kcal",
                           dailyValues       = 1 )
NutriTable.objects.create( product_id    = Product.objects.get(id=1),
                           componentID   = "GORDURAS TOTAIS",
                           componentQuantity = "2.7",
                           componentUM       = "g",
                           dailyValues       = 5 )
NutriTable.objects.create( product_id    = Product.objects.get(id=1),
                           componentID   = "GORDURAS SATURADAS",
                           componentQuantity = "2.4",
                           componentUM       = "g",
                           dailyValues       = 11 )
NutriTable.objects.create( product_id    = Product.objects.get(id=1),
                           componentID   = "SODIO",
                           componentQuantity = "6.8",
                           componentUM       = "mg",
                           dailyValues       = 0 )

# PRODUCT 2
Product.objects.create(id           = 2,
                       name         = "CHOCOLATE EM PO SOLUVEL DOIS FRADES",
                       manufacturer = "NESTLE",
                       barcode      = 7891000451304)

NutriFact.objects.create(product_id      = Product.objects.get(id=1),
                         servingSize     = 2,
                         servingUM       = "COLHERES",
                         servingQuantity = 20,
                         servingQtdUm     = "G",
                         footNote        = "FootNote - footNote")

NutriTable.objects.create( product_id    = Product.objects.get(id=1),
                           componentID   = "VALOR ENERGETICO",
                           componentQuantity = 65,
                           componentUM       = "kcal",
                           dailyValues       = 3 )
NutriTable.objects.create( product_id    = Product.objects.get(id=1),
                           componentID   = "CARBOIDRATOS",
                           componentQuantity = "11",
                           componentUM       = "g",
                           dailyValues       = 4 )
NutriTable.objects.create( product_id    = Product.objects.get(id=1),
                           componentID   = "PROTEINAS",
                           componentQuantity = "2.3",
                           componentUM       = "g",
                           dailyValues       = 3 )
NutriTable.objects.create( product_id    = Product.objects.get(id=1),
                           componentID   = "GORDURAS TOTAIS",
                           componentQuantity = "1.3",
                           componentUM       = "G",
                           dailyValues       = 2 )
NutriTable.objects.create( product_id    = Product.objects.get(id=1),
                           componentID   = "GORDURAS SATURADAS",
                           componentQuantity = "0.7",
                           componentUM       = "G",
                           dailyValues       = 3 )
NutriTable.objects.create( product_id    = Product.objects.get(id=1),
                           componentID   = "GORDURAS TRANS",
                           componentQuantity = "0",
                           componentUM       = "G",
                           dailyValues       = 0 )
NutriTable.objects.create( product_id    = Product.objects.get(id=1),
                           componentID   = "FIBRA ALIMENTAR",
                           componentQuantity = "3.5",
                           componentUM       = "G",
                           dailyValues       = 14 )
NutriTable.objects.create( product_id    = Product.objects.get(id=1),
                           componentID   = "SODIO",
                           componentQuantity = "0",
                           componentUM       = "MG",
                           dailyValues       = 0 )