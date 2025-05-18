from datetime import datetime, timedelta
from django.contrib import admin
from django.utils.html import format_html
from core.environment import env
from common.models import (
    StoredFile,
    StoredFilesGroup
)
from common.forms import (
    StoredFileAdminForm
)
from common.enums import UploaderTypeEnum


@admin.register(StoredFile)
class StoredFileAdmin(admin.ModelAdmin):
    form = StoredFileAdminForm

    list_display = (
        "id",
        "preview",
        "name",
        "ext",
        "download_link",
        # "path",
        "status",
        "hash",
        "uploader_type",
        "uploader_id",
        "stored_files_group",
        "expire_at",
        "created_at",
        "updated_at",
    )

    list_display_links = ("id", "name",)
    search_fields = ("name", "hash")
    list_filter = ("uploader_type", "status")
    ordering = ("-created_at",)

    def save_model(self, request, obj, form, change):
        obj.expire_at = datetime.now() + timedelta(days=30)
        obj.uploader_type = UploaderTypeEnum.ADMIN.value
        obj.uploader_id = request.user.id
        return super().save_model(request, obj, form, change)
    
    def preview(self, obj):
        if obj.ext.lower() in [".png", ".jpg", ".jpeg", ".gif", ".jfif"]:
            return format_html(
                """<img src="{origin}/{path}" style="width:150px; height:150px;"/>""",
                origin=env.get("ORIGIN", "http://localhost:8000"),
                path=obj.path
            )
        return "No Preview"
    preview.short_description = "Preview"

    def download_link(self, obj):
        return format_html(
            """<a href="{origin}/{path}">{path}</a>""",
            origin=env.get("ORIGIN", "http://localhost:8000"),
            path=obj.path
        )
    download_link.short_description = "Download Link"


@admin.register(StoredFilesGroup)
class StoredFilesGroupAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return tuple(field.name for field in self.model._meta.fields)

    search_fields = ("name",)
    list_display_links = ("id", "name",)
    list_filter = ("status",)
    ordering = ("-created_at",)
