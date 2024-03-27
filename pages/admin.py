from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'read') 
    
admin.site.register(ContactMessage, ContactMessageAdmin)
