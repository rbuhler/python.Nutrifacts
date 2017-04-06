from facts.models import NutriFact
from facts.models import NutriTable
from facts.models import Product

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
