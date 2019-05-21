from django.contrib import admin

# Register your models here.
from account.models import UserProfile
from .models import UserProfile
from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','birth','phone')
    list_filter = ("phone",)


admin.site.register(UserProfile,UserProfileAdmin)