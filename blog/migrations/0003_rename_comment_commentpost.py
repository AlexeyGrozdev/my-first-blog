# Generated by Django 3.2.19 on 2023-06-28 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='CommentPost',
        ),
    ]
