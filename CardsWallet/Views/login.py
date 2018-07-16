from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import login, logout
from django.shortcuts import render, redirect
from django.views.generic.base import View
from CardsWallet.forms import LoginForm, SignUpForm
# from CardsWallet.models import UserProfile


class LoginController(View):
    def get(self,request):
        form = LoginForm()
        return render(
            request,
            template_name='login.html',
            context = {'form':form,'title': 'Login'}
        )
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                return redirect('CardsWallet:index')
        return redirect('CardsWallet:login')

def logout_user(request):
     logout(request)
     return redirect('CardsWallet:index')


class SignUpController(View):
    def get(self,request):
        form = SignUpForm()
        return render(
            request,
            template_name='register.html',
            context = {'form':form,'title': 'Signup'}
        )
    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = form.cleaned_data
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('CardsWallet:profile_details_add')
            return redirect('CardsWallet:login')
        else:
            messages.error(request,'Invalid Credentials')


