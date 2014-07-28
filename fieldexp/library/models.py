from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=1, blank=True)
    last_name = models.CharField(max_length=50)

    def __unicode__(self):
        if self.middle_initial == '':
            return '%s %s' % (self.first_name, self.last_name)
        else:
            return '%s %s. %s' % (self.first_name, self.middle_initial, self.last_name)

class Keyword(models.Model):
    keyword = models.CharField(max_length=50)

    def __unicode__(self):
        return self.keyword

class Paper(models.Model):
    file = models.FileField(upload_to='/library/files')
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=256)
    citation = models.CharField(max_length = 256)
    jel = models.CharField(max_length = 256)

    keywords = models.ManyToManyField(Keyword)

    year = models.CharField(max_length = 4, choices= tuple(map(lambda x: (str(x),str(x)), range(1950, 2015))))
    abstract = models.TextField()
    submittee = models.CharField(max_length = 256)
    email = models.EmailField()

    def __unicode__(self):
        return unicode(self.title)
