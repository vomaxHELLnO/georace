from django.contrib import admin
from georace.models import *


class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)


class EventAdmin(admin.ModelAdmin):
    pass
admin.site.register(Event, EventAdmin)
