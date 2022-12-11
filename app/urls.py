
from app.views import index,Signup,Login,logout,events,change_pswd

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('',index,name='homepage'),
    path('signup/',Signup.as_view(),name='signup'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',logout,name='logout'),
    path('add/',events.add_an_event,name='add_event'),
    path('see_you_invited/',events.you_invited,name='you_invited'),
    path('see_you_hosted/',events.events_hosted_by_you,name='you_hosted'),
    path('remove_event/<int:id>',events.remove_event,name='remove_event'),
  
    path('update_event/<int:id>',events.update_event,name='update_event'),
    path('change_password/',change_pswd.change_password,name='change_password'),
    path('search_events',events.search_events,name='search_events'),
    path('date_filter',events.date_filter,name='date_filter')
   

   
]