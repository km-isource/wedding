# Generated by Django 5.1.6 on 2025-02-16 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WedApp', '0009_delete_gallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rsvp',
            name='phone_number',
        ),
    ]
