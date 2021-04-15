from django.db import models

# Create your models here.


class Magazine(models.Model):
    name= models.CharField(max_length=200,null=False)
    published_on= models.DateTimeField()

    def __str__(self):
        return f'Magazine - {self.name}'

class Author(models.Model):
    name = models.CharField(max_length=200,null=False)

    def __str__(self):
        return "Author's name : {}".format(self.name)

class Article(models.Model):
    author= models.ForeignKey(Author, on_delete = models.CASCADE)
    title= models.CharField(max_length=200,null=False)
    magazine= models.ManyToManyField(Magazine,related_name= 'articles')

    def __str__(self):
        return f'Article - {self.title}'
