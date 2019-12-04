from django.contrib import admin
from .models import Event



class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'organizer']
    list_filter = ['start_date', 'organizer']


admin.site.register(Event, EventAdmin)
