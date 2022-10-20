from django.db import models
from django.contrib.auth.models import User


class Articles(models.Model):
    article_title = models.CharField(max_length=200)
    article_sub_title = models.CharField(max_length=200)
    article_body = models.TextField()
    article_pub_date = models.DateTimeField()
    article_banner = models.ImageField(upload_to='media/images/')
    article_votes = models.IntegerField(default=1)


def __str__(self):
    return self.article_title

def summary(self):
    return self.article_body[:200]

def article_pub_date_pretty(self):
    return self.article_pub_date.strftime('%b %e %Y')