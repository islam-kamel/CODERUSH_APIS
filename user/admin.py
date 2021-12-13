from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from user.models import User


class CodeRushUserAdmin(BaseUserAdmin):
    list_display = ['username', 'nickname', 'is_staff']
    list_filter = ['date_join', 'groups', 'is_staff', 'is_superuser']
    readonly_fields = ['date_join', 'last_login']
    fieldsets = (
        (None, {'fields': ('username', 'nickname', 'email', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name', 'phone',
                                         'avatar', 'bio')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_superuser', 'groups',
                                       'user_permissions')}),
        (_('Important Date'), {'fields': ('date_join', 'last_login')}),
        (_('Status'), {'fields': ('is_active',)})
    )

    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': ('username', 'nickname', 'email', 'phone',
                           'password1', 'password2', 'is_staff', 'is_superuser',
                           'is_active')
                }
        ),
    )

    search_fields = ['username', 'phone', 'email']
    filter_horizontal = ['groups', 'user_permissions']


admin.site.register(User, CodeRushUserAdmin)
