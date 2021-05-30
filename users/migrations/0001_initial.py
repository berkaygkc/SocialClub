# Generated by Django 3.2.3 on 2021-05-30 13:40

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_student', models.BooleanField(default=True)),
                ('bio', models.TextField(blank=True)),
                ('address', models.TextField(blank=True)),
                ('bolum', models.TextField(blank=True)),
                ('bolum_baslama', models.DateTimeField(blank=True)),
                ('bolum_bitis', models.DateTimeField(blank=True)),
                ('website', models.TextField(blank=True)),
                ('profile_picture', models.ImageField(blank=True, default='images/default_profile.png', null=True, upload_to='photos', verbose_name='profile photo')),
                ('profile_cover', models.ImageField(blank=True, default='images/default_profile.png', null=True, upload_to='photos', verbose_name='profile cover')),
                ('userId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]