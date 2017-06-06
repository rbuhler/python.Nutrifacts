from facts.models import Product, NutriFact, NutriTable


class DataAccess(object):

    def __init__(self):
        self.products = []
        self.facts = []
        self.table = []

    def all_products(self):
        self.set_products(Product.objects.all())
        self.set_facts(NutriFact.objects.all())
        self.set_table(NutriTable.objects.all())
        return None

    def one_product(self, barcode):
        facts_local = []
        table_local = []
        self.set_products(Product.objects.filter(barcode=barcode))
        if len(self.products) > 0:
            for prod in self.products:
                facts_local.append(NutriFact.objects.filter(product=prod.key))
                table_local.append(NutriTable.objects.filter(product=prod.key))
            self.set_facts(facts_local)
            self.set_table(table_local)
        return None

    def set_products(self, product):
        self.products = product

    def set_facts(self, fact):
        self.facts = fact

    def set_table(self, table):
        self.table = table
