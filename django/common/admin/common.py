from datetime import datetime, timedelta
from django.contrib import admin
from common.models import (
    StoredFile,
    StoredFilesGroup
)
from common.form import (
    StoredFileAdminForm
)
from common.enums import UploaderTypeEnum


@admin.register(StoredFile)
class StoredFileAdmin(admin.ModelAdmin):
    form = StoredFileAdminForm

    def get_list_display(self, request):
        return tuple(field.name for field in self.model._meta.fields)

    list_display_links = ("name",)
    search_fields = ("name", "hash")
    list_filter = ("uploader_type", "status")
    ordering = ("-created_at",)

    def save_model(self, request, obj, form, change):
        obj.expire_at = datetime.now() + timedelta(days=30)
        obj.uploader_type = UploaderTypeEnum.ADMIN.value
        obj.uploader_id = request.user.id
        return super().save_model(request, obj, form, change)


@admin.register(StoredFilesGroup)
class StoredFilesGroupAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("status",)
    ordering = ("-created_at",)
