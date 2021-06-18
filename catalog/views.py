from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product, ProductCategory


class GoodsList(ListView):
    model = Product
    template_name = 'catalog/catalog_list.html'


class CatListItem(ListView):
    model = Product
    template_name = 'catalog/catalog_list.html'

    def get_queryset(self, *args, **kwargs):
        qs = self.model.objects.all()
        if self.kwargs.get('slug'):
            qs = qs.filter(category__slug=self.kwargs['slug'])
        return qs


class ProductDetail(DetailView):
    model = Product
    template_name = 'catalog/catalog_detail.html'


class CategoryDetail(DetailView):
    model = ProductCategory
    template_name = 'catalog/catalog_detail.html'
