from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import News,ViewOnNews # Import Model
from .serializers import NewsSerializer,VideoSerialzier # Import Serializer Class defined in the serializer.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import status
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
    # def create(self,request):
    #     print(request.data)
    #     serializer = VideoSerialzier(data = request.data)
    #     print(serializer)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)        