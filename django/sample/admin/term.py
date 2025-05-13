from django.contrib import admin
from sample.models import (
    Term,
    TermCategory
)


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "term_category",
        "name",
        "version",
        "priority",
        "status",
        "created_at",
        "updated_at"
    )
    search_fields = ("name", "term_category__name")
    list_filter = ("status", "term_category__name")
    ordering = ("-created_at", "-version")

    def term_category(self, obj):
        return obj.term_category.name
    term_category.short_description = "Term Category"


@admin.register(TermCategory)
class TermCategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("status",)
    ordering = ("-created_at",)
