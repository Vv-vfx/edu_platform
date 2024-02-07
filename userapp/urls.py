from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from . import views

app_name = 'userapp'

urlpatterns = [

    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('mainapp:index')), name='logout'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),

]
