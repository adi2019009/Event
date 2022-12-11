from django.contrib import admin

# Register your models here.
from .models import events,invited

admin.site.register(events)
admin.site.register(invited)
