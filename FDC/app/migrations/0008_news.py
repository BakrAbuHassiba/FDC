# Generated by Django 5.1.1 on 2024-10-03 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='news_images/')),
                ('title', models.CharField(max_length=500)),
                ('date', models.CharField(max_length=100)),
                ('paragraph', models.CharField(max_length=500)),
                ('important', models.BooleanField(default=False)),
            ],
        ),
    ]
