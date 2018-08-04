from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    def getTitle(self):
        return self.title

    def getBody(self):
        return self.body
