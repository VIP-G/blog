from django.conf.urls import url,include
from . import views
from .feed import ArticleFeed
app_name = 'blogapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^fullwidth/$', views.fullwidth, name='fullwidth'),
    url(r'^favicon.ico/$', views.favicon),
    url(r'^rss/$',ArticleFeed(),name='name'),


]
