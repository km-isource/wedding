# Generated by Django 5.1.6 on 2025-02-15 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WedApp', '0004_rsvp_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='media',
            name='slide1',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='media',
            name='slide2',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='media',
            name='slide3',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='media',
            name='slide4',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
