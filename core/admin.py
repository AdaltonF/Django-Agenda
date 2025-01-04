from django.contrib import admin
from core.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'creation_date')

admin.site.register(Event, EventAdmin)
