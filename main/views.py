from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
import re
from django.http import HttpResponse
import telebot

from catalog.models import Product
from main.models import Contact

bot = telebot.TeleBot("1396276770:AAF8k9yxEt8yBnfYuBMYR72EQuFGmf_Wvjs", parse_mode='HTML')


class HomePage(View):

    def get(self, request):
        products = Product.objects.filter(is_active=True)
        product_list = products[:5]
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


def subscribe(request):
    import datetime
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%y %H:%M")
    if request.is_ajax():
        phone = request.GET['phone']
        bot.send_message('266087377', f'Новое сообщение:\nphone:\t{phone}\ncallback:\t{now}')
        return HttpResponse(status=200)
    return HttpResponse(status=400)
