# Generated by Django 5.1.1 on 2024-10-02 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_services_icon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='image',
            new_name='images',
        ),
    ]
