# Generated by Django 3.2.5 on 2022-03-28 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Статья')),
                ('content', models.TextField(verbose_name='содержание')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(blank=True, upload_to='')),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Вакансия')),
                ('date_time_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
