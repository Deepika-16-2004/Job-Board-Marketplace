from django.contrib import admin
from .models import UserRole,JobPosting,Resume,Message
# Register your models here.
@admin.register(UserRole,JobPosting,Resume,Message)
class Admin(admin.ModelAdmin):
    list_display=['id']