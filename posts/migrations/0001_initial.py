# Generated by Django 3.2.12 on 2022-03-03 09:23

from django.db import migrations, models
import thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', thumbnails.fields.ImageField(upload_to='')),
                ('description', models.TextField(default='')),
            ],
        ),
    ]
