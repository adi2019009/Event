from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.forms import ValidationError
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def change_password(request):
   
    if request.method == 'GET':
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {'form': form})
    else:
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'change_password.html', {'form': form})
