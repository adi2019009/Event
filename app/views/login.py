
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as loginuser, logout
from django.contrib import messages


class Login(View):
  

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('homepage')
      
        form = AuthenticationForm()
        context = {
            'form': form,
        
        }
        return render(request, 'login.html', context)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('homepage')
      

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginuser(request, user)
                return redirect('homepage')
            
            else:
               
                return render(request, 'login.html', context={'form': form})
        else:
           
            context = {
                'form': form,
            }

            return render(request, 'login.html', context)
