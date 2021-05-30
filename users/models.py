from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    userId = models.OneToOneField(User, on_delete=models.CASCADE)
    is_student = models.BooleanField(default=True, blank=False)
    bio = models.TextField(blank=True)
    address = models.TextField(blank=True)
    bolum = models.TextField(blank=True)
    bolum_baslama = models.TextField(blank=True)
    bolum_bitis = models.TextField(blank=True)
    website = models.TextField(blank=True)
    profile_picture = models.ImageField(null=True,
                                        blank=True,
                                        upload_to='photos',
                                        default='images/default_profile.jpg',
                                        verbose_name='profile photo')
    profile_cover = models.ImageField(null=True,
                                      blank=True,
                                      upload_to='photos',
                                      default='images/default_cover.gif',
                                      verbose_name='profile cover')
    is_completed = models.BooleanField(default=False, blank=False)


class Follows(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    follow = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follow')


