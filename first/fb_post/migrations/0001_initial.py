# Generated by Django 2.2.4 on 2019-08-13 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_profile_pic_url', models.URLField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_description', models.TextField(max_length=400)),
                ('post_at_create', models.DateTimeField(auto_now=True, verbose_name='Post Create Time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', related_query_name='post', to='fb_post.User')),
            ],
            options={
                'unique_together': {('post_description', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_description', models.TextField(max_length=400)),
                ('comment_at_create', models.DateTimeField(auto_now=True, verbose_name='Comment Create Time')),
                ('parent_comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comment', to='fb_post.Comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comment', to='fb_post.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comment', to='fb_post.User')),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction_type', models.CharField(choices=[('LO', 'Love'), ('LI', 'Like'), ('HA', 'Haha'), ('WA', 'Wow'), ('SA', 'Sad'), ('AN', 'Angry')], max_length=6)),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reactions', related_query_name='reaction', to='fb_post.Comment')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reactions', related_query_name='reaction', to='fb_post.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', related_query_name='reaction', to='fb_post.User')),
            ],
            options={
                'unique_together': {('post', 'user'), ('comment', 'user')},
            },
        ),
    ]
