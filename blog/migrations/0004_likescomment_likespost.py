# Generated by Django 3.2.19 on 2023-06-29 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_comment_commentpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikesPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(verbose_name='Число')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_post', to='blog.post')),
            ],
        ),
        migrations.CreateModel(
            name='LikesComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(verbose_name='Число')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_comment', to='blog.commentpost')),
            ],
        ),
    ]