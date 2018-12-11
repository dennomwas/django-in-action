from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from imanichurch.models import User, Designation

class UserAdminPage(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(User, UserAdmin)
