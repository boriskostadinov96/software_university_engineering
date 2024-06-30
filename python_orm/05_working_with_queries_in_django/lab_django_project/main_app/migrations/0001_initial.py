# Generated by Django 5.0.4 on 2024-06-30 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, max_length=50, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('publication_year', models.IntegerField()),
                ('genre', models.CharField(blank=True, max_length=50, null=True)),
                ('language', models.CharField(blank=True, max_length=50, null=True)),
                ('page_count', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(max_length=100)),
                ('book_title', models.CharField(max_length=100)),
                ('author_name', models.CharField(max_length=100)),
                ('rating', models.PositiveIntegerField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
