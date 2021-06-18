from django.urls import path

from main.views import AboutPage, ContactPage, subscribe

urlpatterns = [
    path('about/', AboutPage.as_view(), name="about"),
    path('contact/', ContactPage.as_view(), name="contacts"),
    path('ajax/', subscribe, name="subscribe")
]