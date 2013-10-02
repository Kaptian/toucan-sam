import random
from django.template.defaulttags import register

CSS_COLORS = [
    'gold',
    'fuchsia',
    'hotpink',
    'lime',
    'orangered',
    'red',
    'sienna',
    'darkorchid'
]

@register.simple_tag()
def randocolor():
    return random.choice(CSS_COLORS)