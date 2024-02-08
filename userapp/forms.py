from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MyUser
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email", None)

        if email is None:
            raise forms.ValidationError(_('Введите email'))
        if MyUser.objects.filter(email=email).exists():
            raise forms.ValidationError(
                _(f'Пользователь с email {email} уже зарегистрирован. Если Вы забыли пароль нажмите "Сменить пароль"'))
        return email

    def save(self, commit=True):
        print('зашел в save')
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
            Token.objects.get_or_create(user=user)
        return user


class MyUserLoginForm(AuthenticationForm):
    pass

