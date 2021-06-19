from django import template
import re

register = template.Library()


@register.filter('intspace')
def intspace(value):
    """
        Converts an integer to a string containing spaces every three digits.
        For example, 3000 becomes '3 000' and 45000 becomes '45 000'.
        See django.contrib.humanize app
    """
    new = '{0:,}'.format(value).replace(',', ' ')
    if value == new:
        return value
    else:
        return new