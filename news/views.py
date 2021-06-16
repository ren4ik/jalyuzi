from django.shortcuts import render
from django.views.generic import ListView, DetailView

from news.models import Article


class NewsList(ListView):
    model = Article
    template_name = 'news/news_list.html'


class NewsDetail(DetailView):
    model = Article
    template_name = 'news/news_detail.html'
    slug_url_kwarg = 'slug'
