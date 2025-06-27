from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'user_type', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('user_type',)
admin.site.register(User, UserAdmin)


