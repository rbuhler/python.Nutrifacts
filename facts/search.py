import elasticsearch as elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text
from . import models

connections.create_connection()


class ProductIndex(DocType):
    name = Text()
    manufacturer = Text()
    barcode = Text()


def bulk_indexing():
    ProductIndex.init()
    es = elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.Product.objects.all().iterator()))


# Add indexing method to BlogPost
def indexing(self):
    obj = ProductIndex(
      meta={'id': self.id},
      name=self.name,
      manufacturer=self.manufacturer,
      barcode=self.barcode
    )
    obj.save()
    return obj.to_dict(include_meta=True)
