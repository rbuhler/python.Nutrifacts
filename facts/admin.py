from django.contrib import admin
from .models import Product
from .models import NutriFact
from .models import NutriTable


# Register your models here.

admin.site.register(Product)
admin.site.register(NutriFact)
admin.site.register(NutriTable)
