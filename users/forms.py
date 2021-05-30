from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input',
                                                             'placeholder': 'Lütfen kullanıcı adınızı giriniz'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input',
                                                            'placeholder': 'Lütfen e-Posta adresinizi giriniz'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input',
                                                                 'placeholder': 'Lütfen Şifrenizi giriniz'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input',
                                                                        'placeholder': 'Lütfen Şifrenizi tekrar giriniz'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input',
                                                               'placeholder': 'Lütfen Adınızı giriniz'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input',
                                                              'placeholder': 'Lütfen Soyadınızı giriniz'}))


class RegisterComplete(forms.Form):
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'input',
                                                       'placeholder': 'Kendinizden bahsedin'}), required=False, max_length=500)
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'input',
                                                            'placeholder': 'Adresinizi giriniz'}), required=False, max_length=100)
    bolum = forms.CharField(widget=forms.TextInput(attrs={'class': 'input',
                                                            'placeholder': 'Okuduğunuz bölümü giriniz'}), max_length=100)
    bolum_baslama = forms.DateField(widget=forms.TextInput(attrs={'class': 'input', 'type': 'date'}))
    bolum_bitis = forms.DateField(widget=forms.TextInput(attrs={'class': 'input', 'type': 'date'}))
    website = forms.CharField(widget=forms.TextInput(attrs={'class': 'input',
                                                          'placeholder': 'Websitenizi giriniz'}), required=False)


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input',
                                                             'placeholder': 'Lütfen kullanıcı adınızı giriniz'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input',
                                                             'placeholder': 'Lütfen şifrenizi giriniz'}))


class SettingsForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-fade'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-fade'}))
    bolum = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-fade'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-fade'}), required=False)
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'input is-fade'}), required=False)
    web = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-fade'}), required=False)