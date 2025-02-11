from django.contrib import admin
from .models import Thread, Message



@admin.register(Thread)
class Thread(admin.ModelAdmin):
    list_display = ('participants', 'created_date', 'updated', 'user')
    list_filter = ('participants', )


@admin.register(Message)
class Message(admin.ModelAdmin):
    list_display = ('sender', 'text', 'thread', 'created', 'is_read')
    search_fields = ('text', )
    list_filter = ('is_read', )