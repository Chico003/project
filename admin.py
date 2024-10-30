from django.contrib import admin # type: ignore
from .models import Project, Event, Member

admin.site.register(Project)
admin.site.register(Event)
admin.site.register(Member)
