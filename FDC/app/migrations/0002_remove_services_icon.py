# Generated by Django 5.1.1 on 2024-10-02 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='icon',
        ),
    ]
