from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html, format_html_join
from core.environment import env
from sample.models import (
    Store,
    StoreCategory,
    StoreCharacterPool
)
from sample.form import StoreAdminForm


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    class Media:
        js = (
            f"https://oapi.map.naver.com/openapi/v3/maps.js?ncpKeyId={env.get('NCP_KEY_ID')}&submodules=geocoder",
        )
    form = StoreAdminForm

    list_display = (
        "id",
        "title",
        "address",
        "store_category_list",
        "coordinate",
        "business_day_list",
        "pre_order_start_at",
        "opening_time",
        "closing_time",
        "status",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id", "title")
    search_fields = ("title", "address")
    list_filter = ("status",)
    ordering = ("-created_at",)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("store_categories")

    def store_category_list(self, obj):
        categories = obj.store_categories.all()
        return format_html(
            "<ul style='margin:0; padding-left:16px;'>{}</ul>",
            format_html_join("", "<li>{}</li>", ((category.name,) for category in categories))
        )
    store_category_list.short_description = "Category List"

    def coordinate(self, obj):
        return mark_safe(f"""
            <div id="naver-map-{obj.id}" style="width:150px; height:150px;"></div>
            <script>
                const map{obj.id} = new naver.maps.Map('naver-map-{obj.id}', {{
                    center: new naver.maps.LatLng({obj.latitude}, {obj.longitude}),
                    zoom: 16,
                    scaleControl: false,
                    mapDataControl: false
                }});
                const marker{obj.id} = new naver.maps.Marker({{
                    position: new naver.maps.LatLng({obj.latitude}, {obj.longitude}),
                    map: map{obj.id}
                }});
            </script>
        """)
    coordinate.short_description = "Coordinate"

    def business_day_list(self, obj):
        DAY_CHOICES = [
            (1, "일"),
            (2, "월"),
            (4, "화"),
            (8, "수"),
            (16, "목"),
            (32, "금"),
            (64, "토"),
        ]
        days = [label for value, label in DAY_CHOICES if obj.business_day & value]
        return ", ".join(days)
    business_day_list.short_description = "Business Day List"


@admin.register(StoreCategory)
class StoreCategoryAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return tuple(field.name for field in self.model._meta.fields)
    search_fields = ("name",)
    ordering = ("-created_at",)


@admin.register(StoreCharacterPool)
class StoreCharacterPoolAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "store_title",
        "character_name",
        "weight",
        "status",
        "created_at",
        "updated_at"
    )
    search_fields = ("store__title", "character__name")
    list_filter = ("status",)
    ordering = ("-created_at",)

    def store_title(self, obj):
        return obj.store.title
    store_title.short_description = "Store Title"

    def character_name(self, obj):
        return obj.character.name
    character_name.short_description = "Character Name"
