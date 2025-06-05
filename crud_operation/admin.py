from django.contrib import admin
from .models import UserStudent
# Register your models here.
@admin.register(UserStudent)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password')
