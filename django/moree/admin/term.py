from django.contrib import admin
from moree.models import (
    Term,
    TermCategory
)


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "term_category",
        "agreement_type",
        "name",
        "version",
        "priority",
        "hash",
        "created_at",
        "updated_at"
    )
    list_display_links = ("id", "name")
    search_fields = ("name", "term_category__name")
    list_filter = ("term_category__name",)
    ordering = ("-created_at", "-version")

    def term_category(self, obj):
        return obj.term_category.name
    term_category.short_description = "Term Category"


@admin.register(TermCategory)
class TermCategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    ordering = ("-created_at",)
