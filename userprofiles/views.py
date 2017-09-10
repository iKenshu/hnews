from django.shortcuts import render, redirect

from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

from .forms import SignUpAndSignInForm
from .models import Profile

# Create your views here.

class SignUpView(CreateView):
    model = Profile
    form_class = SignUpAndSignInForm
    template_name = 'registration.html'

    def form_valid(self, form):
        form.save()
        return redirect('New:list')

class SignInView(LoginView):
    template_name = 'login.html'
    
class SignOutView(LogoutView):
    pass