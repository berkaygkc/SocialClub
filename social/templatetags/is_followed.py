from django import template

from users.models import Follows

register = template.Library()


@register.simple_tag(name='is_followed')
def is_followed(user, club):
    return Follows.objects.filter(user_id=user, follow_id=club).exists()