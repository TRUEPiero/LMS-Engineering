from django import template
import Study.views as views
import os

register =template.Library()

@register.filter(name='file')
def getextension(value):
    split_tup = os.path.splitext(value)
    return split_tup[1][1:]


@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)
