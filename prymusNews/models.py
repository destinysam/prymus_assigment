from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class News(models.Model): # Defining the News model
    title = models.CharField(max_length=150)
    content = models.TextField()
    category = models.CharField(max_length=100)
    tags = models.TextField()
    dated = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self): # Dunder Method or Magic Method
        return self.title


class ViewOnNews(models.Model):
    news = models.ForeignKey(News,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    videofile = models.FileField(upload_to="uploaded-videos",null=True)
    dated = models.DateTimeField(auto_now_add=True)
    video_tags = models.CharField(max_length=200)
    video_likes = models.IntegerField(null=True)

    def __str__(self):
        return self.news.title


