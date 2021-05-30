import profile

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from .models import Post
from users.models import Follows
from social.forms import NewPost


@login_required(login_url='/Login')
def index(request):
    try:
        if request.user.profile.is_completed:
            form = NewPost(request.POST or None)
            if form.is_valid():
                body = form.cleaned_data['body']
                post = Post(body=body, userId_id=request.user.id)
                post.save()
                form = NewPost()
            posts = Post.objects.filter(userId__follow__user_id=request.user.id).order_by('-created_at')
            clubs = User.objects.filter(profile__is_student=0)
            return render(request, 'index.html', {
                'posts': posts,
                'clubs': clubs,
                'form': form
            })
        else:
            return HttpResponseRedirect('/RegisterComplete')
    except:
        return HttpResponseRedirect('/RegisterComplete')


def follow(request, username=None):
    club = User.objects.get(username=username)
    user = User.objects.get(username=request.user.username)
    follow = Follows.objects.filter(user_id=user.id, follow_id=club.id).exists()
    if not follow:
        newFollow = Follows(user_id=user.id, follow_id=club.id)
        newFollow.save()
    return HttpResponseRedirect('/Club/'+club.username)


def unfollow(request, username=None):
    club = User.objects.get(username=username)
    user = User.objects.get(username=request.user.username)
    follow = Follows.objects.filter(user_id=user.id, follow_id=club.id).exists()
    if follow:
        followItem = Follows.objects.get(user_id=user.id, follow_id=club.id)
        followItem.delete()
    return HttpResponseRedirect('/Club/'+club.username)