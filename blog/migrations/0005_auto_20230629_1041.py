# Generated by Django 3.2.19 on 2023-06-29 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_likescomment_likespost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likescomment',
            name='value',
        ),
        migrations.RemoveField(
            model_name='likespost',
            name='value',
        ),
        migrations.AddField(
            model_name='commentpost',
            name='username',
            field=models.CharField(default='admin', max_length=32, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='likescomment',
            name='username',
            field=models.CharField(default='admin', max_length=32, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='likespost',
            name='username',
            field=models.CharField(default='admin', max_length=32, verbose_name='Текст'),
        ),
    ]