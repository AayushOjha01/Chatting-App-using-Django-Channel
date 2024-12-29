from django.contrib import admin
from .models import chatGroup, Usergroup, Message

# Register your models here.
admin.site.register(chatGroup)
admin.site.register(Usergroup)
admin.site.register(Message)