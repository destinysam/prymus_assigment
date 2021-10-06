from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter() # Using DefaultRouter to show additonal api root view 
# Using routers to build Url
router.register("News",views.NewsView)
router.register("videoViews",views.VideoView,basename="ViewOnNews")

urlpatterns = [
    path("",include(router.urls)),
    path("postVideo/",views.PostVideo,name="VideoList")
]