from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from users.models import Profile, Follows
from social.models import Post

from .forms import RegisterForm, RegisterComplete, LoginForm, SettingsForm
from social.forms import NewPost


def profile(request, username=None):
    user = get_object_or_404(User, username=username)
    if user.profile.is_student:
        return render(request, "users/profile.html", {'user': user})
    else:
        return HttpResponseRedirect('/Club/'+user.username)


def loginpage(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    template = "users/login.html"
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if not Follows.objects.filter(follow_id=user.id, user_id=user.id).exists():
                follow = Follows(follow_id=user.id, user_id=user.id)
                follow.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, template, {
                'form': form,
                'error_message': 'Kullanıcı Adı yada Şifre hatalı!'
            })
    else:
        return render(request, template, {
            'form': form
        })


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')


    template = "users/register.html"

    if request.method == "POST":
        form = RegisterForm(request.POST)
        # Formun geçerli olup olmadığı kontrol edilir:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Kullanıcı adı kullanımda! Başka bir kullanıcı adı giriniz!'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'e-Posta daha önce kullanılmış! Lütfen başka bir e-Posta giriniz!'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Şifreler eşleşmiyor!'
                })
            else:
                # Kullanıcı Kaydı Oluşturulur:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()

                # Giriş Yaptırılır:
                login(request, user)

                # Diğer bilgiler ekranına yönlendirilir:
                return HttpResponseRedirect('/RegisterComplete/')
        else:
            return render(request, template, {
                'form': form,
                'error_message': 'Form Geçersiz! Lütfen tüm alanları doldurunuz!'
            })
    else:
        form = RegisterForm()
        return render(request, template, {'form': form})


def registercomplete(request):
    try:
        if request.user.profile.is_completed:
            return HttpResponseRedirect('/')
    except:
        pass

    template = 'users/registerDetail.html'

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = RegisterComplete(request.POST)
            if form.is_valid():
                userId = request.user.id
                bio = form.cleaned_data['bio']
                bolum = form.cleaned_data['bolum']
                bolum_bas = form.cleaned_data['bolum_baslama'],
                bolum_bit = form.cleaned_data['bolum_bitis']
                address = form.cleaned_data['address']
                website = form.cleaned_data['website']
                try:
                    if not request.user.profile.is_completed:
                        prof = Profile.objects.filter(id=request.user.profile.id).first()
                        prof.bio = bio
                        prof.bolum=bolum
                        prof.bolum_baslama=bolum_bas
                        prof.bolum_bitis=bolum_bit
                        prof.address=address
                        prof.website=website
                        prof.is_completed=True
                        prof.save()
                except:
                    prof = Profile(userId_id=userId, bio=bio, bolum=bolum, bolum_baslama=bolum_bas, bolum_bitis=bolum_bit,
                                   address=address, website=website, is_completed=True)
                    prof.save()


                return HttpResponseRedirect('/')
            else:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Form Geçersiz! Lütfen zorunlu alanları doldurunuz!'
                })
        else:
            return HttpResponseRedirect('/Login')
    else:
        form = RegisterComplete()
        return render(request, template, {'form': form})


@login_required(login_url='/Login')
def logoutuser(request):
    logout(request)
    return HttpResponseRedirect("/")


@login_required(login_url='/Login')
def settings(request):
    template = "users/settings.html"

    form = SettingsForm(request.POST or None)

    if form.is_valid():
        adi = form.cleaned_data['first_name']
        soyadi = form.cleaned_data['last_name']
        bolum = form.cleaned_data['bolum']
        adres = form.cleaned_data['address']
        bio = form.cleaned_data['bio']
        web = form.cleaned_data['web']
        try:
            user = User.objects.get(id=request.user.id)
            user.first_name = adi
            user.last_name = soyadi
            user.save()
            prof = Profile.objects.filter(id=request.user.profile.id).first()
            prof.bio = bio
            prof.bolum = bolum
            prof.address = adres
            prof.website = web
            prof.save()
            return HttpResponseRedirect('/Profile/' + request.user.username)
        except:
            return HttpResponseRedirect('/Profile/' + request.user.username)
    else:
        initial_dict = {
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "bolum": request.user.profile.bolum,
            "address": request.user.profile.address,
            "bio": request.user.profile.bio,
            "web": request.user.profile.website
        }
        form.initial = initial_dict
        return render(request, template, {
            'form': form
        })


@login_required(login_url='/Login')
def clubprofile(request, username=None):
    club = get_object_or_404(User, username=username)
    if club.profile.is_student:
        return HttpResponseRedirect('/Profile/'+club.username)
    else:
        form = NewPost(request.POST or None)
        if form.is_valid():
            body = form.cleaned_data['body']
            post = Post(body=body, userId_id=request.user.id)
            post.save()
            form = NewPost(None)
        posts = Post.objects.order_by('-created_at').filter(userId_id=club.id)
        if request.user.id != club.id:
            return render(request, "clubs/profile-user.html", {
                'club': club,
                'posts': posts
            })
        else:
            return render(request, "clubs/profile-club.html", {
                'club': club,
                'posts': posts,
                'form': form
            })


@login_required(login_url='/Login')
def clubdetail(request, username=None):
    club = get_object_or_404(User, username=username)
    return render(request, "clubs/club-about.html", {
        'club': club
    })
