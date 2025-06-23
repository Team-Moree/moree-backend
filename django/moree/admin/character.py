from django.contrib import admin
from moree.models import (
    Character
)


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return tuple(field.name for field in self.model._meta.fields)
    search_fields = ("name",)
    list_display_links = ("id", "name",)
    ordering = ("-created_at",)
