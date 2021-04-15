from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article_api',ArticleViewSet,basename = 'article')
urlpatterns=[
# path('articles/',ArticleViewSet.as_view()),
# path('magazines/',MagazineViewSet.as_view()),
# path('author/',AuthorViewSet.as_view()),
path('articles/',ArticleList,name='article_list'),
path('magazines/',MagazineList,name='magazine_list'),
path('authors/<pk>/articles/',Author_ArticleDetail,name = 'article_detail'),
path('magazines/<pk>/articles/',Magazine_ArticleDetail,name = 'article_detail'),
path('',include(router.urls))

]
