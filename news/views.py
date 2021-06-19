from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q

from news.models import Article


class NewsList(ListView):
    model = Article
    template_name = 'news/news_list.html'
    queryset = model.objects.filter(Q(is_active=True) & Q(category__is_active=True))


class NewsDetail(DetailView):
    model = Article
    template_name = 'news/news_detail.html'
    slug_url_kwarg = 'slug'


class ArticleListItem(ListView):
    model = Article
    template_name = 'news/news_list.html'

    def get_queryset(self, *args, **kwargs):
        qs = self.model.objects.all()
        if self.kwargs.get('slug'):
            qs = qs.filter(Q(category__slug=self.kwargs['slug']) & Q(is_active=True))
        return qs
