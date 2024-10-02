# your_app/models.py

from django.db import models


class Service(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    bgImg = models.ImageField(upload_to='bg_images/')
    icon = models.ImageField(upload_to='icons/')
    txt = models.CharField(max_length=100)
    subTitle = models.TextField(max_length=500, null=True)
    paragraph = models.TextField(max_length=500,null=True)
    points = models.JSONField(null=True)  # Store points in JSON format

    def __str__(self):
        return self.txt


class Project(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    projectImg = models.ImageField(upload_to='project_images/')
    projectTitle = models.CharField(max_length=500)
    date = models.CharField(max_length=100)
    client = models.CharField(max_length=100)

    def __str__(self):
        return self.projectTitle
