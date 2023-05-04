from django.contrib import admin

from .models import CustomUser, Organization


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone',
                    'image', 'is_active', 'is_staff',
                    'is_superuser'
                    )


class OrganizationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Organization, OrganizationsAdmin)
