from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("allNews",views.NewsView)
router.register("searchnews",views.SearchNews)
urlpatterns = [
    path("",include(router.urls))
]