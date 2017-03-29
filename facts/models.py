from django.db import models

# Create your models here.


class Product(models.Model):
    id = models.PositiveIntegerField(primary_key=True)

    name = models.CharField(max_length=60)
    manufacturer = models.CharField(max_length=60)
    barcode = models.PositiveIntegerField()


class NutriFact(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)

    servingSize = models.FloatField()
    servingUM = models.CharField(max_length=4)
    servingQuantity = models.FloatField()
    servingQtdUm = models.CharField(max_length=4)
    footNote = models.TextField()


class NutriTable(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    index = models.AutoField(primary_key=True)

    componentID = models.CharField(max_length=60)
    componentQuantity = models.FloatField()
    componentUM = models.CharField(max_length=4)
    dailyValues = models.FloatField()
