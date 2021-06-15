from django.urls import path

from main.views import AboutPage, ContactPage

urlpatterns = [
    path('about/', AboutPage.as_view(), name="about"),
    path('contact/', ContactPage.as_view(), name="contact")
]