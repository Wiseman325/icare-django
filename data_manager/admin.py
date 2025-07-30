from django.contrib import admin

# Register your models here.
from .models import Case, CaseType, roomForum, topic, Message, User, Status

admin.site.register(User)
admin.site.register(Case)
admin.site.register(CaseType)
admin.site.register(roomForum)
admin.site.register(topic)
admin.site.register(Message)
admin.site.register(Status)