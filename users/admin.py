from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'phone', 'is_staff']

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ['phone']}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ['first_name', 'last_name', 'phone']}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
