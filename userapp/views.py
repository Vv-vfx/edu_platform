from urllib.parse import unquote, quote

from django import forms

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from .forms import MyUserCreationForm, MyUserLoginForm
from django.contrib.auth import login
from rest_framework.authtoken.models import Token
from django.utils.http import url_has_allowed_host_and_scheme
from .models import MyUser


class UserRegisterView(CreateView):
    form_class = MyUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('mainapp:index')  # URL для перенаправления после успешной регистрации

    def form_valid(self, form):
        # Этот метод вызывается, когда валидные данные формы были отправлены

        # вызываем родительский метод и здесь же вызывается save() из MyUserCreationForm
        response = super().form_valid(form)

        # # Получаем сохраненный объект пользователя из метода формы save()
        user = self.object
        # если user есть - логин
        if user is not None:
            # Автоматический вход после регистрации
            login(self.request, user)

        return response


class UserLoginView(LoginView):
    form_class = MyUserLoginForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        # Получаем параметр `next` из запроса
        next_url = self.request.POST.get('next')
        print(next_url)

        # Проверяем, указан ли URL в параметре `next` и является ли он безопасным
        # функция url_has_allowed_host_and_scheme проверяет, принадлежит ли url нашему сайту

        if next_url and url_has_allowed_host_and_scheme(
                url=next_url,
                allowed_hosts={self.request.get_host()},
                require_https=self.request.is_secure()
        ):

            return next_url
        else:
            # Если параметр `next` не указан, используем значение из success_url
            return reverse_lazy('mainapp:index')


class UserProfileView(LoginRequiredMixin, DetailView):
    model = MyUser
    template_name = 'registration/profile.html'
    context_object_name = 'MyUser'

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        # Получаем контекст от базового класса
        context = super().get_context_data(**kwargs)
        # Добавляем токен в контекст, если пользователь авторизован
        if self.request.user.is_authenticated:
            token = Token.objects.get(user=self.request.user)
            context['token'] = token.key
        else:
            context['token'] = 'Пользователь не авторизован'

        return context
