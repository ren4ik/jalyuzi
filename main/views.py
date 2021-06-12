from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class HomePage(View):

    def get(self, request):
        return render(request, 'index.html')


class AboutPage(TemplateView):
    pass


class ContactPage(View):
    pass

