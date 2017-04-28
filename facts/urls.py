from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^product/([0-9]{13})$', views.product_detail, name='product_detail'),
]