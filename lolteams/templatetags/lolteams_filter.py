from django import template

register = template.Library()

@register.filter
def mul(value, arg):
    return round(value * 100)