# Generated by Django 2.1 on 2018-08-16 05:49

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180816_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='文章正文'),
        ),
    ]