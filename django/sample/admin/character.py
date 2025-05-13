from django.contrib import admin
from sample.models import (
    Character
)


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("status",)
    ordering = ("-created_at",)
