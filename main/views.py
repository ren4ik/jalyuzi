from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from catalog.models import Product


class HomePage(View):

    def get(self, request):
        products = Product.objects.filter(is_active=True)
        product_list = products[:4]
        new_product = products.filter(is_new=True).first()
        return render(request, 'home.html', {
            'product_list': product_list,
            'new_product': new_product
        })


class AboutPage(TemplateView):

    def get(self, request):
        return render(request, 'main/about.html')


class ContactPage(View):

    def get(self, request):
        return render(request, 'main/contacts.html')

