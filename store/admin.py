from django.contrib import admin
from .models import Box
# Register your models here.

@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    pass
