from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from app.forms import eventForm
from app.models import events,invited
from django.contrib.auth.models import User

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')
