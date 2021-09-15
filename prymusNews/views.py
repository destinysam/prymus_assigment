from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import News
from .serializers import NewsSerializer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class NewsView(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ["tags","title","content"]
    filterset_fields = ["category"]
    queryset = News.objects.all()
    print(len(queryset))