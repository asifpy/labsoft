from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def undertospaced(value):
    return value.replace("_", " ").title()

@register.filter
def get_model_fields(obj):
    return obj._meta.fields

@register.filter
def get_value(obj, field):
    return getattr(obj, field)
