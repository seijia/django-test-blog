from  django import template
register = template.Library()  #　自定义filter时必须加上


@register.filter(name="lower2")
def lower2(value):
    return value.lower()