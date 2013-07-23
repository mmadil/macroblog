from django import template
from urlparse import urlparse

register = template.Library()


def website(url):
    u = urlparse(url)
    return u[1]

