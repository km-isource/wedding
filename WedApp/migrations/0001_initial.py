# Generated by Django 5.1.6 on 2025-02-14 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/')),
                ('uploader_name', models.CharField(max_length=100)),
                ('uploader_email', models.EmailField(max_length=254)),
                ('approved', models.BooleanField(default=False)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('video', models.FileField(blank=True, null=True, upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=100)),
                ('attendance', models.CharField(choices=[('yes', 'Yes, I will attend'), ('no', 'No, I will not attend')], max_length=100)),
                ('guest_count', models.PositiveBigIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WeddingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bride', models.CharField(max_length=100)),
                ('groom', models.CharField(max_length=100)),
                ('day', models.CharField(max_length=100)),
                ('before_date', models.DateField(blank=True, null=True)),
                ('date', models.DateField()),
                ('after_date', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('ceremony_time', models.TimeField()),
                ('ceremony_venue', models.CharField(max_length=100)),
                ('ceremony_location', models.CharField(max_length=100)),
                ('reception_name', models.CharField(max_length=100)),
                ('reception_location', models.CharField(max_length=100)),
                ('reception_time', models.TimeField()),
            ],
        ),
    ]
