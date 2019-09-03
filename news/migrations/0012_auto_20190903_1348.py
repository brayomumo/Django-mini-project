# Generated by Django 2.1.11 on 2019-09-03 10:48

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20190903_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='post',
            field=tinymce.models.HTMLField(default='post'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='news.Tags'),
        ),
    ]
