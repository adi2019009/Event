from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logoutuser

@login_required(login_url='login')
def logout(request):
    logoutuser(request)
    return redirect('login')
    