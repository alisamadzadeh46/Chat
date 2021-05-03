from django.contrib import admin
from .models import Message


@admin.register(Message)
class AdminMessage(admin.ModelAdmin):
    list_display = ['username', 'room']
