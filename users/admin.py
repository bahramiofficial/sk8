from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import  User


class UserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = User
    list_display = ('mobile',   'is_staff', 'is_active',)
    list_filter = ('mobile', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('mobile',)
    # ordering = ('email',)


admin.site.register(User, UserAdmin)
