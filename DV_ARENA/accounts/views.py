from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .models import Account
from .forms import Signupform,SigninForm
from django.contrib.auth.models import User



class SignupView(CreateView):
    model = Account
    form_class=Signupform
    template_name='signup.html'
    success_url=reverse_lazy('signin')


class SigninView(LoginView):
    form_class=SigninForm
    template_name='sign-in.html'
    success_url=reverse_lazy('home')