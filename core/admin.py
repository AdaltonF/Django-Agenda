from django.contrib import admin
from core.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'creation_date', 'user')

admin.site.register(Event, EventAdmin)
