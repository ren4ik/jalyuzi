from django import template
from news.models import NewsCategory
register = template.Library()


@register.inclusion_tag('main/new_tags.html')
def news_in_site():
    menu_list = NewsCategory.objects.filter(is_active=True)[:5]
    return {
        'menu_list': menu_list,
    }
