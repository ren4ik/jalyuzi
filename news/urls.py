from django.urls import path

from news.views import NewsList

urlpatterns = [
    path('news', NewsList.as_view(), name="news")
]