from rest_framework import serializers
from .models import *

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"

class MagazineSerializers(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = "__all__"
