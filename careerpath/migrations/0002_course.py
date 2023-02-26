# Generated by Django 4.1.7 on 2023-02-25 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careerpath', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=128)),
                ('image_link', models.CharField(max_length=512)),
                ('description', models.CharField(max_length=1024)),
            ],
        ),
    ]