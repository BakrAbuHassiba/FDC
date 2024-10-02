# your_app/serializers.py

from .models import Project
from rest_framework import serializers
from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    serviceData = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ['id', 'bgImg', 'icon', 'txt', 'serviceData']

    def get_serviceData(self, obj):
        return {
            # Get URL of the image if it exists
            'bgImg': obj.bgImg.url if obj.bgImg else None,
            # Get URL of the icon if it exists
            'icon': obj.icon.url if obj.icon else None,
            'title': obj.txt,                                 # Use 'txt' as 'title'
            'subTitle': obj.subTitle,
            'paragraph': obj.paragraph,
            'points': obj.points
        }




class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'projectImg', 'projectTitle', 'date', 'client']
