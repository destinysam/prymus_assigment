from django.db import models

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
