from django.urls import path

from catalog.views import GoodsList, ProductDetail, CategoryDetail, CatListItem

urlpatterns = [
    path('goods/', GoodsList.as_view(), name="catalog"),
    path('product/<slug:slug>/', ProductDetail.as_view(), name="product-detail"),
    path('category/<slug:slug>/', CategoryDetail.as_view(), name="category-product-detail"),
    path('tag-product/<slug:slug>/', CatListItem.as_view(), name="product-tag")
]