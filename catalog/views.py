from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q

from catalog.models import Product, ProductCategory


class GoodsList(ListView):
    model = Product
    template_name = 'catalog/catalog_list.html'
    queryset = model.objects.filter(Q(is_active=True) & Q(category__is_active=True))
    paginate_by = 6


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

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        category = self.model.objects.get(slug=self.kwargs['slug'])
        context['categories'] = self.model.objects.filter(
            Q(is_active=True) & Q(category=category.category)
        )
        return context


class CategoryDetail(DetailView):
    model = ProductCategory
    template_name = 'catalog/catalog_detail.html'
