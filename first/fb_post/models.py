from django.db import models


# Create your models here.


class CommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(parent_comment=None)


class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(post__isnull=False)


class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_profile_pic_url = models.URLField(max_length=400)

    def __str__(self):
        return self.user_name


class Post(models.Model):
    post_description = models.TextField(max_length=400)
    post_at_create = models.DateTimeField('Post Create Time', auto_now=True, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', related_query_name='post')

    class Meta:
        unique_together = ['post_description', 'user']

    def __str__(self):
        return self.post_description


class Comment(models.Model):
    comment_description = models.TextField(max_length=400)
    comment_at_create = models.DateTimeField('Comment Create Time', auto_now=True, editable=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='comments',
                                       related_query_name='comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')

    def __str__(self):
        return self.comment_description

    objects = models.Manager()
    onlycomments = CommentManager()


class Reaction(models.Model):
    reaction_types = [
        ('LO', 'Love'),
        ('LI', 'Like'),
        ('HA', 'Haha'),
        ('WA', 'Wow'),
        ('SA', 'Sad'),
        ('AN', 'Angry'),
    ]
    reaction_type = models.CharField(max_length=6, choices=reaction_types)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions', related_query_name='reaction',
                             null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reactions',
                                related_query_name='reaction', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reactions', related_query_name='reaction')

    class Meta:
        unique_together = [['post', 'user'], ['comment', 'user']]

    def __str__(self):
        return self.reaction_type

    objects = models.Manager()
    postReactions = PostManager()