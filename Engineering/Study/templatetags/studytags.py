from django import template
import Study.views as views

register =template.Library()

@register.simple_tag()
def getcategories():
    return views.exercise
