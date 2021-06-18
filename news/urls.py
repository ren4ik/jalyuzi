from django.urls import path

from news.views import NewsList, NewsDetail, ArticleListItem

urlpatterns = [
    path('articales/', NewsList.as_view(), name="news"),
    path('article/<slug:slug>/', NewsDetail.as_view(), name="article-detail"),
    path('tag-article/<slug:slug>/', ArticleListItem.as_view(), name="article-tag")
]