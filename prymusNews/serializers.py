from rest_framework import serializers
from .models import News,ViewOnNews # importing our Model
# Using serializers to convert complex data(querysets) into python datatypes

class NewsSerializer(serializers.ModelSerializer): # Defining Serializer Class
    class Meta:
        model = News # Reprsents Our Model
        fields = "__all__"  # All fields to show

class VideoSerialzier(serializers.ModelSerializer):
    news = serializers.CharField(source="news.title", read_only=True)
    author = serializers.CharField(source="author.username",read_only=True)
    class Meta:
        model =  ViewOnNews
        fields = ["news","author","videofile","dated","video_likes"]
