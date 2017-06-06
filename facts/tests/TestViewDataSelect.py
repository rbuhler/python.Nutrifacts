from django.test import TestCase
from facts.models import Product


class TestViewDataSelect(TestCase):
    @staticmethod
    def setup():
        Product.objects.create(id=1, name='Product1', manufacturer='Manufacturer', barcode=1234567890123)
