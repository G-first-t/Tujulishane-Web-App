from django.contrib import admin

# Register your models here.
from .models import ReminderStatus,Student,Parent, Issue
admin.site.register(ReminderStatus)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Issue)