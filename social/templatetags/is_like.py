from django import template

from social.models import Like

register = template.Library()


@register.simple_tag(name='is_liked')
def is_liked(user, post):
    return Like.objects.filter(userId_id=user, postId_id=post).exists()
