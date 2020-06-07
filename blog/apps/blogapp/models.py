from django.db import models

from DjangoUeditor.models import UEditorField


# Create your models here.
class Adds(models.Model):
    img = models.ImageField(upload_to='ads', verbose_name='图片')
    desc = models.CharField(max_length=20, null=True, blank=True, verbose_name='图片描述')

    def __str__(self):
        return self.desc


class Catalog(models.Model):
    name = models.CharField(max_length=10, verbose_name='分类名')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=10, verbose_name='标签名')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=10, verbose_name='文章标题')
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, verbose_name='分类')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_data = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    author = models.CharField(max_length=10, verbose_name='作者')
    views = models.IntegerField(default=0, verbose_name='浏览量')
    # body = models.TextField(verbose_name='正文')
    # 百度附文本类型
    body = UEditorField(imagePath='imgs/', width='100%', verbose_name='正文')

    tags = models.ManyToManyField(Tag, verbose_name='标签')

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=10, verbose_name='名字')
    url = models.URLField(default='http://zgh.com', verbose_name='网址')
    email = models.EmailField(default='1969563601@qq.com', verbose_name='邮箱')
    body = models.CharField(max_length=50, verbose_name='评论内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='所属文章')

    def __str__(self):
        return self.name
