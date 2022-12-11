from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from app.forms import eventForm
from app.models import invited, events
from django.db.models import Q

from django.core.paginator import Paginator


@login_required(login_url='login')
def add_an_event(request):
    user = request.user
    form = eventForm(request.POST,initial={'host':request.user.id})

    if form.is_valid():
        event=form.save()
        print(form.cleaned_data.get('host'))
        for t in event.invited_user.all():
            invtd = invited(user=t, event=event)
            invtd.save()

        return redirect('add_event')

    else:
        print(form.errors)
        return render(request, 'add_an_event.html', context={'form': form})


@login_required(login_url='login')
def you_invited(request):
    user = request.user
    obj = invited.objects.filter(user=user)
    p = Paginator(obj, 2)
    page = request.GET.get('page')
    obj = p.get_page(page)
    context = {
        'objs': obj,
    }
    return render(request, 'see_events_you_invited.html', context)


@login_required(login_url='login')
def events_hosted_by_you(request):
    sort_events = request.GET.get('sort_events')
    date_filter = request.GET.get('date_filter')

    user = request.user

    if sort_events is not None:
        obj = events.objects.filter(host=user).order_by('date', 'time')
    else:
        obj = events.objects.filter(host=user)

    p = Paginator(obj, 4)
    page = request.GET.get('page')
    obj = p.get_page(page)

    context = {
        'objs': obj,
        'sort_events': sort_events,
        'date_filter': date_filter
    }

    return render(request, 'see_events_hosted_by_you.html', context)


@login_required(login_url='login')
def search_events(request):
    user = request.user
    if request.method == "POST":
        searched = request.POST.get('searched')

        obj = events.objects.filter(Q(event_name__icontains=searched))

        context = {
            'searched': searched,
            'objs': obj,

        }
        return render(request, 'search_events.html', context)

    else:
        return render(request, 'search_events.html', {})


@login_required(login_url='login')
def remove_event(request, id):
        obj = events.objects.get(pk=id).delete()
        return redirect('you_hosted')


@login_required(login_url='login')
def update_event(request, id):
    event = events.objects.get(pk=id)
    form = eventForm(request.POST or None, instance=event)
    if form.is_valid():
        event = form.save()
        invited.objects.filter(event=event).delete()
        for t in event.invited_user.all():
            invtd = invited(user=t, event=event)
            invtd.save()

        return redirect('you_hosted')

    else:
        return render(request, 'update_event.html', context={'event': event, 'form': form})



    


@login_required(login_url='login')
def date_filter(request):
    if request.method == "POST":
        obj = events.objects.filter(date=request.POST.get('date'))

        return render(request, 'filter_by_date.html', context={'objs': obj})
