from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from api.models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    list_display = (
        "email",
        "enrolment_no",
        "username",
        "year",
        "is_member",
        "is_staff",
        "is_superuser",
    )
    list_filter = ("is_staff", "is_superuser", "is_member")
    fieldsets = (
        (None, {"fields": ("email", "enrolment_no", "username", "year", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_member")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "enrolment_no",
                    "username",
                    "year",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_superuser",
                    "is_member",
                ),
            },
        ),
    )
    search_fields = ("email", "enrolment_no", "username")
    ordering = ("email",)


admin.site.register(User, UserAdmin)
admin.site.register(project)
admin.site.register(task)
admin.site.register(goal)
admin.site.register(feedback)

# Register your models here.
