from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.forms import CustomUserCreationForm
from accounts.models import CustomUser
from django.utils.translation import gettext_lazy as _




@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        ('Birth Year', {'fields': ('birth_year',)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),(
        'Birth Year', {'fields': ('birth_year',)},
    )
    )