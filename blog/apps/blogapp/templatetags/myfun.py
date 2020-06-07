from django.template import Library
from blogapp.models import Article, Catalog, Tag
register = Library()



@register.filter
def dataFormat(data):
    return '%d-%d-%d' % (data.year, data.month, data.day)


@register.filter
def authorFormat(author, info):
    return info + ':' + author.upper()


@register.simple_tag
def get_latearticles(num=3):
    return Article.objects.all().order_by('-create_time')[:num]


@register.simple_tag
def get_laterdata(num=3):
    dates = Article.objects.dates('create_time', 'month', 'DESC', )[:num]
    return dates


@register.simple_tag
def get_catagorys():
    return Catalog.objects.all().order_by('-id')

@register.simple_tag
def get_tags():
    return Tag.objects.all().order_by('-id')
