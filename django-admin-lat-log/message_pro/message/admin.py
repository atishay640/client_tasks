from django.contrib import admin
from .models import Message
from django.contrib.auth.models import User

admin.site.unregister(User)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'latitude', 'longitude',)
    search_fields = ('message',)
    exclude = ['uuid']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email')
    search_fields = ('username',)
    