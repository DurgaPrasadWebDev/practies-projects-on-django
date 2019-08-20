from django.db.models import *

from .models import *


class PostException(Exception):
    def __init__(self, error):
        self.error = error


class CommentException(Exception):

    def __int__(self, error):
        self.error = error


class UserException(Exception):
    def __init__(self, error):
        self.error = error


class ReactionException(Exception):
    def __init__(self, error):
        self.error = error


def user_details_fetch(user_details):
    user = dict()
    user["user_id"] = user_details.id
    user["name"] = user_details.user_name
    user["profile_pic_url"] = user_details.user_profile_pic_url
    return user


def reaction_details_fetch(reactions_details):
    reactions = dict()
    reactions_type_list = []
    total_reaction = 0
    for each_reaction in reactions_details:
        reaction_type = each_reaction.get_reaction_type_display()
        if reaction_type not in reactions_type_list:
            reactions_type_list.append(reaction_type)
        total_reaction += 1
    reactions["count"] = total_reaction
    reactions["type"] = reactions_type_list
    return reactions


def comment_convert_to_dictionary(comment, no_replies, replies):
    comment_details = dict()
    comment_details["comment_id"] = comment.id
    comment_details["commenter"] = user_details_fetch(comment.user)
    comment_details["commented_at"] = time_convert_to_string(comment.comment_at_create)
    comment_details["comment_content"] = comment.comment_description
    comment_details["reactions"] = reaction_details_fetch(comment.reactions.all())
    comment_details["replies_count"] = no_replies
    comment_details["replies"] = replies
    return comment_details


def reply_convert_to_dictionary(reply):
    reply_details = dict()
    reply_reactions_details = reaction_details_fetch(reply.reactions.all())
    reply_details["comment_id"] = reply.id
    reply_details["commenter"] = user_details_fetch(reply.user)
    reply_details["commented_at"] = time_convert_to_string(reply.comment_at_create)
    reply_details["comment_content"] = reply.comment_description
    reply_details["reactions"] = reply_reactions_details
    return reply_details


def post_convert_to_dictionary(post, comments, no_comments):
    user_details = post.user
    user = user_details_fetch(user_details)
    if user_details is None:
        raise UserException('User Detail Not Found')
    post_details = dict()
    post_details["post_id"] = post.id
    post_details["posted_by"] = user
    post_details["posted_at"] = time_convert_to_string(post.post_at_create)
    post_details["post_content"] = post.post_description
    post_details["reactions"] = reaction_details_fetch(Reaction.objects.select_related().filter(post=post))
    post_details["comments"] = comments
    post_details["comments_count"] = no_comments
    return post_details


def time_convert_to_string(time):
    return time.strftime("%d-%b-%Y %H:%M:%S.%f")


def fetch_post_object(post_id):
    try:
        return Post.objects.get(id=post_id)
    except ObjectDoesNotExist:
        raise PostException('The Post Object Does Not Found with given Post_id')


def fetch_user_object(user_id):
    try:
        return User.objects.select_related().get(id=user_id)
    except ObjectDoesNotExist:
        raise UserException('The User Object Does Not Found with given User_id')


def fetch_comment_object(comment_id):
    try:
        return Comment.objects.select_related().get(id=comment_id)
    except ObjectDoesNotExist:
        raise CommentException('The Comment Object Does Not Found with given Comment_id')


def get_post_details(post):
    comments_of_post = post.comments.all()#Comment.objects.filter(post=post).annotate(
    #     reaction_type_count=Count('reaction')).select_related('user', 'parent_comment').prefetch_related('reactions')
    total_comments = []
    for each_comment in comments_of_post:
        if each_comment.parent_comment:
            continue
        replies = []
        for each_reply in comments_of_post:
            if each_reply.parent_comment and each_reply.parent_comment == each_comment:
                reply_details = reply_convert_to_dictionary(each_reply)
                replies.append(reply_details)
        no_replies = len(replies)
        comment_details = comment_convert_to_dictionary(each_comment, no_replies, replies)
        total_comments.append(comment_details)
    comment_count = len(total_comments)
    post = post_convert_to_dictionary(post, total_comments, comment_count)
    return post


def get_post(post_id):
    post_details = fetch_post_object(post_id)
    posts = Post.objects.filter(id=post_details.id).select_related('user').prefetch_related('comments', 'comments__reactions',
                                                                                   'comments__user', 'reactions',
                                                                                   'comments__parent_comment',
                                                                                   'comments__parent_comment')
    post = get_post_details(posts[0])
    return post


def create_post(user_id, post_content):
    user = fetch_user_object(user_id)
    post = user.posts.create(post_description=post_content)
    return post.id


def add_comment(post_id, comment_user_id, comment_text):
    post = fetch_post_object(post_id)
    user = fetch_user_object(comment_user_id)
    comment = post.comments.create(comment_description=comment_text, user=user)
    return comment.id


def reply_to_comment(comment_id, reply_user_id, reply_text):
    comment = fetch_comment_object(comment_id)
    user = fetch_user_object(reply_user_id)
    post = comment.post
    if comment.parent_comment is not None:
        comment = comment.parent_comment
    reply_comment = Comment.objects.create(comment_description=reply_text, parent_comment=comment, post=post,
                                           user=user)
    return reply_comment.id


def react_to_comment(user_id, comment_id, reaction_type):
    user = fetch_user_object(user_id)
    comment = fetch_comment_object(comment_id)
    try:
        reaction = Reaction.objects.get(comment=comment, user=user)
        if reaction.reaction_type == reaction_type:
            reaction.delete()
        else:
            reaction.reaction_type = reaction_type
            reaction.save()
            return reaction.id
    except ObjectDoesNotExist:
        reaction = Reaction.objects.create(reaction_type=reaction_type, comment=comment, user=user)
        return reaction.id


def react_to_post(user_id, post_id, reaction_type):
    user = fetch_user_object(user_id)
    post = fetch_post_object(post_id)
    try:
        reaction = Reaction.objects.get(post=post, user=user)
        if reaction.reaction_type == reaction_type:
            reaction.delete()
        else:
            reaction.reaction_type = reaction_type
            reaction.save()
            return reaction.id
    except ObjectDoesNotExist:
        reaction = Reaction.objects.create(reaction_type=reaction_type, post=post, user=user)
        return reaction.id


def get_user_posts(user_id):
    user = fetch_user_object(user_id)
    posts = Post.objects.filter(user=user).select_related('user').prefetch_related('comments','comments__reactions', 'comments__user','reactions','comments__parent_comment','comments__parent_comment')
    if posts.count() == 0:
        raise PostException('The User Does Not Create Any Posts So Their is Empty Posts')
    list_of_posts = []
    for each_post in posts:
        # user = each_post.user
        # comments = each_post.comments.all()
        # for each_comment in comments:
        #     each_comment_details = each_comment.id
        #     reaction = each_comment.reactions.all()
        list_of_posts.append(get_post_details(each_post))
    return list_of_posts


def get_posts_with_more_positive_reactions():
    positive_reaction_count = Count('reaction', filter=Q(reaction__reaction_type__in=['LI', 'LO', 'HA', 'WO']))
    negative_reaction_count = Count('reaction', filter=Q(reaction__reaction_type__in=['SA', 'AN']))

    posts_with_reactions = Post.objects.annotate(positive_reaction_count=positive_reaction_count,
                                                 negative_reaction_count=negative_reaction_count)
    posts_with_more_positive_reactions = posts_with_reactions.filter(
        positive_reaction_count__gte=F('negative_reaction_count'))
    list_of_posts_id = posts_with_more_positive_reactions.values_list('id', flat=True)
    return list_of_posts_id


def get_posts_reacted_by_user(user_id):
    user = fetch_user_object(user_id)
    reactions = Reaction.objects.filter(user=user).select_related('post')
    post_id_list = []
    for each_reaction in reactions:
        if each_reaction.post is None:
            continue
        post_id_list.append(each_reaction.post_id)
    return post_id_list


def get_reactions_to_post(post_id):
    post = fetch_post_object(post_id)
    reactions = Reaction.objects.filter(post=post)
    reactions_with_user = reactions.annotate(
        name=F('user__user_name'), profile_pic_url=F('user__user_profile_pic_url'), reaction=F('reaction_type'))
    user_details = reactions_with_user.values('user_id', 'name', 'profile_pic_url', 'reaction')
    return user_details


def get_reaction_metrics(post_id):
    post = fetch_post_object(post_id)
    reaction_metrics = Reaction.objects.filter(post=post).values('reaction_type').annotate(
        reaction_count=Count('reaction_type'))
    return reaction_metrics


def get_total_reaction_count():
    reaction_count = Reaction.postReactions.count()
    return reaction_count


def delete_post(post_id):
    deleted_post = fetch_post_object(post_id).delete()
    return deleted_post


def get_replies_for_comment(comment_id):
    comment = fetch_comment_object(comment_id)
    replies_objects = Comment.objects.filter(parent_comment=comment).annotate(
        reaction_type_count=Count('reaction')).select_related('user').prefetch_related('reactions')
    replies = []
    for each_reply in replies_objects:
        replies_with_user = reply_convert_to_dictionary(each_reply)
        replies.append(replies_with_user)
    return replies