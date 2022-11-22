from django.contrib import admin
from .models import Contact


# Register your models here.

class AdminContact(admin.ModelAdmin):
    list_display = ('full_name', 'email',)


admin.site.register(Contact, AdminContact)
