from django import forms

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from .forms import MyUserCreationForm, MyUserLoginForm
from django.contrib.auth import login, authenticate

from .models import MyUser



class UserRegisterView(CreateView):
    form_class = MyUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('mainapp:index')  # URL для перенаправления после успешной регистрации

    def form_valid(self, form):
        # Этот метод вызывается, когда валидные данные формы были отправлены
        user = form.save()
        print('before login')
        # user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(self.request, user)  # Автоматический вход после регистрации
        print(user)
        print('after login')
        return super().form_valid(form)


class UserLoginView(LoginView):
    print(1111111111)
    form_class = MyUserLoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('mainapp:index')  # URL для перенаправления после успешной регистрации



class UserProfileView(LoginRequiredMixin, DetailView):
    model = MyUser
    template_name = 'registration/profile.html'
    context_object_name = 'MyUser'

    def get_object(self):
        print(self.request.user)
        return self.request.user
