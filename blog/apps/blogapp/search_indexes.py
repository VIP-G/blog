from haystack import indexes
# 指明搜索模型Article

from .models import Article


# 1.类名必须为模型名+Index
# 2.get_model必须返回模型名
class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
