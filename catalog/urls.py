from django.urls import path

from catalog.views import GoodsList

urlpatterns = [
    path('catalog/', GoodsList.as_view(), name="catalog")
]