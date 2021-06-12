from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class HomePage(View):
    pass


class AboutPage(TemplateView):
    pass


class ContactPage(View):
    pass

