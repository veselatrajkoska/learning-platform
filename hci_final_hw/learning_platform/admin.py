from django.contrib import admin
from .models import *

# Register your models here.

class PlatformUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'profile_picture')

admin.site.register(PlatformUser, PlatformUserAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'image')

admin.site.register(Course, CourseAdmin)
