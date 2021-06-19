from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse
import telebot

from catalog.models import Product
from main.models import Contact, Slider, Command
from news.models import Article
from jalyuzi.local_settings import KEY_TELEGRAM

bot = telebot.TeleBot(KEY_TELEGRAM, parse_mode='HTML')


class HomePage(View):

    def get(self, request):
        slides = Slider.objects.filter(is_active=True)
        products = Product.objects.filter(is_active=True)
        product_list = products[:5]
        new_product = products.filter(is_new=True).first()
        popular = products.filter(is_popular=True)
        populars = popular[:3]
        populars_2 = popular[:5]
        popular_product = products.filter(is_popular=True).first()
        articles = Article.objects.filter(is_active=True)[:5]
        return render(request, 'home.html', {
            'product_list': product_list,
            'new_product': new_product,
            'populars': populars,
            'populars_2': populars_2,
            'popular_product': popular_product,
            'articles': articles,
            'slides': slides
        })


class AboutPage(TemplateView):

    def get(self, request):
        slides = Slider.objects.filter(is_active=True)
        commands = Command.objects.filter(is_active=True)
        return render(request, 'main/about.html', {
            'slides': slides,
            'commands': commands
        })


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
