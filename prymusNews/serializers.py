from rest_framework import serializers
from .models import News # importing our Model
# Using serializers to convert complex data(querysets) into python datatypes

class NewsSerializer(serializers.ModelSerializer): # Defining Serializer Class
    class Meta:
        model = News # Reprsents Our Model
        fields = "__all__"  # All fields to show