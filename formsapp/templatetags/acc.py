from django import template
register = template.Library()

@register.inclusion_tag(filename='recomm.html', takes_context=True)
def acc(indexable, i):
    return indexable[i]