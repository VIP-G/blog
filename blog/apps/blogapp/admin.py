from django.contrib import admin

# Register your models here.
from .models import Article, Comment, Catalog, Adds, Tag

admin.site.register(Adds)
admin.site.register(Article)
admin.site.register(Catalog)
admin.site.register(Comment)
admin.site.register(Tag)
