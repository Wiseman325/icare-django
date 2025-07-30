from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Case, CaseType, roomForum, topic, Message, User, Status

# Custom UserAdmin with role support
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_superuser')
    list_filter = ('role', 'is_staff')
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('role', 'phone_number', 'avatar')}),
    )

# Unregister User if already registered
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

# Register models
admin.site.register(User, CustomUserAdmin)
admin.site.register(Case)
admin.site.register(CaseType)
admin.site.register(roomForum)
admin.site.register(topic)
admin.site.register(Message)
admin.site.register(Status)
