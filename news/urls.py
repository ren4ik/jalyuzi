from django.urls import path

from news.views import NewsList, NewsDetail

urlpatterns = [
    path('articales/', NewsList.as_view(), name="news"),
    path('article/<slug:slug>/', NewsDetail.as_view(), name="article-detail")
]