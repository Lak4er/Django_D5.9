# Generated by Django 4.1.4 on 2022-12-10 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_rating', models.IntegerField(default=0, null=True)),
                ('author_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in_post', models.DateTimeField(auto_now_add=True)),
                ('event', models.CharField(choices=[('NS', 'Новость'), ('PP', 'Статья')], max_length=2)),
                ('title', models.CharField(max_length=199)),
                ('post_text', models.TextField()),
                ('post_rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPortal.category')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPortal.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(through='NewsPortal.PostCategory', to='NewsPortal.category'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPortal.author'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in_comment', models.DateTimeField(auto_now_add=True)),
                ('comment_text', models.TextField(unique=True)),
                ('comment_rating', models.IntegerField(default=0)),
                ('comment_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPortal.post')),
                ('comment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
