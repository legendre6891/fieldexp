from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=1, blank=True)
    last_name = models.CharField(max_length=50)

class Keyword(models.Model):
    keyword = models.CharField(max_length = 20)

class Paper(models.Model):
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=256)
    citation = models.CharField(max_length = 256)
    JEL = models.CharField(max_length = 256)
    keywords = models.ManyToManyField(Keyword)
    year = models.CharField(max_length = 4, choices= tuple(map(lambda x: (str(x),str(x)), range(1950, 2015))))
    abstract = models.TextField()
    submittee = models.CharField(max_length = 256)
    email = models.EmailField()

