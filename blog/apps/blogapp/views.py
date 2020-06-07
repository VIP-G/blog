from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import *
from .forms import *
from django.core.paginator import Page, Paginator
import time
from datetime import datetime


# 一个Page中有  object_list代表当前页的所有对象
# has_next 是不是有下一页
# has_previous 是否有上一页
# next_page_number 下一页的编号
# previous_page_number 上一页的编号
# self.number 当前页的编号
# self.paginator 当前页的分页器


# 一个Paginator中的object_list 代表所有未分页对象
# self.per_page 每一页有几个对象
# get_page(self, number): 从分页器中取第几页
# page_range(self): 返回分页列表


# Create your views here.
def index(res):
    ads = Adds.objects.all()

    typepage = res.GET.get('type')
    # print('当前页面类型', typepage)
    year = None
    month = None
    category_id = None
    if typepage == 'date':
        year = res.GET.get('year')
        month = res.GET.get('month')
        articles = Article.objects.filter(create_time__year=year, create_time__month=month).order_by('-create_time')
    elif typepage == 'category':
        category_id = res.GET.get('category_id')
        print(category_id + '+++')
        try:
            category = Catalog.objects.get(id=category_id)
            articles = category.article_set.all()
        except Exception as e:
            print(e)
            return HttpResponse('分类不合法')
    elif typepage == 'tag':
        tag_id = res.GET.get('tag_id')
        try:
            tag = Tag.objects.get(id=tag_id)
            articles = tag.article_set.all()
        except Exception as e:
            print(e)
            return HttpResponse('标签不合法')

    else:
        articles = Article.objects.all().order_by('-create_time')
        # locals()可以返回作用域局部变量
    paginator = Paginator(articles, 2)
    num = res.GET.get('pagenum',1)

    page = paginator.get_page(num)
    # for pa in page.object_list:
    #     time = pa.create_time
    #
    #     strtime = time.strftime('%Y-%m-%d %H:%M:%S')
    return render(res, 'index.html', locals())


def detail(res, articleid):
    if res.method == 'GET':
        try:
            article = Article.objects.get(id=articleid)
            cf = CommentForm()
            return render(res, 'single.html', locals())
        except Exception as e:
            print(e)
            return HttpResponse('文章不合法')
    elif res.method == 'POST':
        cf = CommentForm(res.POST)
        if cf.is_valid():
            comment = cf.save(commit=False)
            comment.article = Article.objects.get(id=articleid)
            comment.save()
            url = reverse('blogapp:detail', args=(articleid,))
            return redirect(to=url)
            # articleid = Article.objects.get(id=articleid)
            # cf = CommentForm()
            # return render(res, 'single.html', locals())
        else:
            article = Article.objects.get(id=articleid)
            cf = CommentForm()
            error = '输入信息有误'
            return render(res, 'single.html', locals())


def contact(res):
    return render(res, 'contact.html')


# 返回logo
def favicon(res):
    return redirect(to='/static/favicon.ico')
def fullwidth(res):
    return render(res,'full-width.html')