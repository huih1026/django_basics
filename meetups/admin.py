from meetups.models import Location, Meetup, Participant
from django.contrib import admin

# Register your models here.


class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title', )
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)
