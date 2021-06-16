from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product, ProductCategory


class GoodsList(ListView):
    model = Product
    template_name = 'catalog/catalog_list.html'


class ProductDetail(DetailView):
    model = Product
    template_name = 'catalog/catalog_detail.html'


class CategoryDetail(DetailView):
    model = ProductCategory
    template_name = 'catalog/catalog_detail.html'


class ProductTagList(ListView):
    model = Product
    template_name = 'catalog/catalog_list.html'
