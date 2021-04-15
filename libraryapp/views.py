from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response
from .models import *
from rest_framework import viewsets

@api_view(['GET'])
def ArticleList(request):
    articles = Article.objects.all()
    serializer = ArticleSerializers(articles,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def MagazineList(request):
    magazines = Magazine.objects.all()
    serializer = MagazineSerializers(magazines,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Author_ArticleDetail(request,pk):
    articles = Article.objects.filter(author__id=pk)
    serializer = ArticleSerializers(articles,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Magazine_ArticleDetail(request,pk):
    articles = Article.objects.filter(magazine__id=pk)
    serializer = ArticleSerializers(articles,many=True)
    return Response(serializer.data)


class ArticleViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = ArticleSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Article is Created')
        return Response(serializer.error,status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        article = Article.objects.get(id=pk)
        serializer = ArticleSerializers(article)
        return Response(serializer.data)

    def update(self, request, pk=None):
        article = Article.objects.get(id=pk)
        serializer = ArticleSerializers(article,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Article is Updated')
        return Response(serializer.error,status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        article = Article.objects.get(id=pk)
        article.delete()
        return Response('Article is deleted')
