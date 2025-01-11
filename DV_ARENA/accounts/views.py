from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Account
from .forms import Signupform
# Create your views here.
class SignupView(CreateView):
    form_class=Signupform
    template_name='signup.html'
    success_url=reverse_lazy('home')

