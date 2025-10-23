from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # 🧩 Display section
    list_display = (
        "id",
        "email",
        "username",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
        "date_joined",
    )
    list_display_links = ("email", "username")
    list_filter = ("is_active", "is_staff", "is_superuser", "date_joined")
    ordering = ("-date_joined",)

    # 🔍 Search
    search_fields = ("email", "username", "first_name", "last_name", "phone_number")

    # 🕓 Read-only fields (non-editable)
    readonly_fields = ("date_joined", "updated_at", "last_login")

    # 🧱 Field grouping on the user edit page
    fieldsets = (
        (_("Account Info"), {
            "fields": ("email", "username", "password")
        }),
        (_("Personal Information"), {
            "fields": ("first_name", "last_name", "phone_number"),
        }),
        (_("Permissions & Roles"), {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions"),
        }),
        (_("Important Dates"), {
            "fields": ("last_login", "date_joined", "updated_at"),
        }),
    )

    # ➕ Fieldsets when adding a new user
    add_fieldsets = (
        (_("Create New User"), {
            "classes": ("wide",),
            "fields": (
                "email",
                "username",
                "first_name",
                "last_name",
                "phone_number",
                "password1",
                "password2",
                "is_staff",
                "is_active",
            ),
        }),
    )

    # 🧠 Extra touches for admin UX
    save_on_top = True  # shows save buttons on top and bottom
    list_per_page = 20  # pagination in admin list view



# not too beautifull layout 
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active')

    list_display_links = ('email', 'username', 'first_name', 'last_name')
    
    # Make non-editable fields readonly
    readonly_fields = ('date_joined', 'updated_at', 'last_login')

    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('date_joined', 'updated_at', 'last_login')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

"""



# old code

"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_admin', 'is_staff', 'is_active', 'date_joined')
    list_display_links = ('email', 'username', 'first_name', 'last_name')

    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)

"""