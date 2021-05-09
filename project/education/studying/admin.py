from django.contrib import admin

# Register your models here.
from studying.models import CourseListener, ListenerAnswer

admin.site.register(CourseListener)
admin.site.register(ListenerAnswer)
