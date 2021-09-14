from django.shortcuts import render
from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer
# Create your views here.
class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.filter(title="prymus").order_by("-dated")
    serializer_class = NewsSerializer



