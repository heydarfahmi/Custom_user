from django.contrib import admin
from user.models import CustomUser


class CustomUserAdminPanel(admin.ModelAdmin):
    list_display = ('username','first_name', 'last_name',)
    list_filter = ('is_staff','is_superuser','last_login',)
    list_per_page = 20
    exclude = ('last_login')
admin.site.register(CustomUser,CustomUserAdminPanel)


# Register your models here.
