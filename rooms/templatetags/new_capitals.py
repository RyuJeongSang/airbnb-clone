from django import template

register = template.Library()


@register.filter()
def new_capitals(value):
    return value.capitalize()