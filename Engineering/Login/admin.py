from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from . import models

@admin.register(models.User)
class AdminUser(UserAdmin):
    fieldsets = (
        (None, {
            "fields": (
                'username','first_name','last_name',
                'email','password','is_superuser','is_staff','is_active',
                'groups','user_permissions',
                'photo','study_group',
                'date_joined','last_login',

            ),
        }),
    )

admin.site.register(models.StudentGroup)
