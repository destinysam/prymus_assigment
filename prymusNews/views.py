from django.shortcuts import render
from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by("-dated")
    serializer_class = NewsSerializer

class SearchNews(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["tags","title","content"]
    queryset = News.objects.all().order_by("-dated")