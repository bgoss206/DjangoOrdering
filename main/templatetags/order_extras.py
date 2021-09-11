from django import template
from django.template.defaulttags import register

register = template.Library()

@register.filter
def get_quantity(dictionary, key):
    return dictionary[key]

@register.filter(name='zip')
def zip_lists(a, b):
    return zip(a, b)