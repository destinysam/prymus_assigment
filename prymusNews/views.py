from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import News,ViewOnNews # Import Model
from .serializers import NewsSerializer,VideoSerialzier # Import Serializer Class defined in the serializer.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.serializers import Serializer
from django.contrib.auth.models import User
class NewsView(viewsets.ModelViewSet): # View Class
    serializer_class = NewsSerializer # Serializer Class
    pagination_class = LimitOffsetPagination # Controlling Limit and offset in the view level
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ["tags","title","content"] # DRF-Api TASK 2
    filterset_fields = ["category"] # DRF-Api Task 1
    queryset = News.objects.all().order_by("-dated") # DRF-Api Task 3
    # Response Time < 60 
#    print(len(queryset)) # Check queryset length
class VideoView(viewsets.ModelViewSet):
    serializer_class = VideoSerialzier
    def get_queryset(self):
        id= self.request.GET.get('id')
        queryset = ViewOnNews.objects.filter(news=id)
        return queryset  
    # @csrf_exempt     
    # def create(self,request):
    #     print(request.data)
    #     serializer = VideoSerialzier(data = request.data)
    #     print(serializer)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)        
@csrf_exempt
@api_view(["POST"])
def PostVideo(request):
    news = request.data.get("news")
    author = request.data.get("author")
    videofile = request.data.get("videofile")
    video_tags = request.data.get("video_tags")
    video_likes = request.data.get("video_likes")
    news1 = News.objects.get(pk=int(news))
    author1 = User.objects.get(pk=int(author))
    viewVideo = ViewOnNews.objects.create(news=news1,author=author1,videofile=videofile,video_tags=video_tags,video_likes=video_likes)
    viewVideo.save()
    return Response(status=status.HTTP_201_CREATED)
    
    
