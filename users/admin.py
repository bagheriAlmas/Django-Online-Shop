from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm  # dokmeye add kardan yek user
    form = CustomUserChangeForm  # formi ke haminjuri aval be ma neshun mide
    model = CustomUser
    list_display = ['username', 'email', 'phone', ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('gender', 'phone', 'avatar', 'postal_code', 'address'), }),)  # baraye ChangeForm
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('gender', 'phone', 'avatar', 'postal_code', 'address'), }),)  # baraye CreationForm


admin.site.register(CustomUser, CustomUserAdmin)
