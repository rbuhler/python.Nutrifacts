from django.db import models

# Create your models here.


class Product(models.Model):
    key = models.PositiveIntegerField(primary_key=True)

    name = models.CharField(max_length=60)
    manufacturer = models.CharField(max_length=60)
    barcode = models.PositiveIntegerField()


class NutriFact(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)

    servingSize = models.FloatField()
    servingUM = models.CharField(max_length=4)
    servingQuantity = models.FloatField()
    servingQtdUm = models.CharField(max_length=4)
    footNote = models.TextField()


class NutriTable(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)

    componentID = models.CharField(max_length=60)
    componentQuantity = models.FloatField()
    componentUM = models.CharField(max_length=4)
    dailyValues = models.FloatField()
