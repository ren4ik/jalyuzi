from django import template
from catalog.models import ProductCategory
register = template.Library()


@register.inclusion_tag('main/tag_list.html')
def menu_in_site():
    menu_list = ProductCategory.objects.filter(is_active=True)[:10]
    return {
        'menu_list': menu_list,
    }
