# your_app/serializers.py

from .models import Project, Service, News
from rest_framework import serializers



class ServiceSerializer(serializers.ModelSerializer):
    serviceData = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ['id', 'bgImg', 'txt', 'serviceData']

    def get_serviceData(self, obj):
        return {
            # Get URL of the image if it exists
            'bgImg': obj.bgImg.url if obj.bgImg else None,
            # Get URL of the icon if it exists
            'title': obj.txt,                                 # Use 'txt' as 'title'
            'subTitle': obj.subTitle,
            'paragraph': obj.paragraph,
            'points': obj.points
        }




class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'projectImg', 'projectTitle', 'date', 'client', 'important']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'image', 'title', 'date', 'paragraph','important']
