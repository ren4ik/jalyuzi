from django.contrib import admin

from news.models import Article, NewsCategory


@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
        'admin_image',
        'description',
        'pub_date',
        'is_active',
    ]
    list_per_page = 20
    list_editable = [
        'is_active',
        'description',
    ]


@admin.register(NewsCategory)
class AdminNewsCategory(admin.ModelAdmin):
    list_display = [
        'name',
        'is_active',
    ]
    list_per_page = 20
    list_editable = [
        'is_active',
    ]

