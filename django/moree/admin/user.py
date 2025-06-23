from django.contrib import admin
from moree.models import (
    User,
    UserAccessToken,
    UserRefreshToken,
    UserCharacterInventory,
    UserFolloing,
    UserTermAgreement,
    UserReview,
    UserReviewReport,
    UserStoreStamp,
    UserStoreBookmark,
    UserStoreCategory,
    UserLog,
    UserSMSVerification,
    UserSMSVerificationRequest,
    UserSMSVerificationRecord
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return tuple(field.name for field in self.model._meta.fields)
    search_fields = ("name", "email", "phone")
    list_display_links = ("id", "name",)
    ordering = ("-created_at",)


@admin.register(UserAccessToken)
class UserAccessTokenAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return tuple(field.name for field in self.model._meta.fields)


@admin.register(UserRefreshToken)
class UserRefreshTokenAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return tuple(field.name for field in self.model._meta.fields)


@admin.register(UserCharacterInventory)
class UserCharacterInventoryAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return tuple(field.name for field in self.model._meta.fields)


@admin.register(UserFolloing)
class UserFolloingAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return tuple(field.name for field in self.model._meta.fields)


@admin.register(UserTermAgreement)
class UserTermAgreementAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return tuple(field.name for field in self.model._meta.fields)
    
    search_fields = ("user__name", "term__name")
    ordering = ("-created_at",)


@admin.register(UserReview)
class UserReviewAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return tuple(field.name for field in self.model._meta.fields)


@admin.register(UserReviewReport)
class UserReviewReportAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return tuple(field.name for field in self.model._meta.fields)


@admin.register(UserStoreStamp)
class UserStoreStampAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return tuple(field.name for field in self.model._meta.fields)


@admin.register(UserStoreBookmark)
class UserStoreBookmarkAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return tuple(field.name for field in self.model._meta.fields)
    
    search_fields = ("user__name", "store__title", "title")
    list_display_links = ("id", "title")
    list_filter = ("visibility",)


@admin.register(UserStoreCategory)
class UserStoreCategoryAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return tuple(field.name for field in self.model._meta.fields)


@admin.register(UserLog)
class UserLogAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return tuple(field.name for field in self.model._meta.fields)


@admin.register(UserSMSVerification)
class UserSMSVerificationAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return tuple(field.name for field in self.model._meta.fields)


@admin.register(UserSMSVerificationRequest)
class UserSMSVerificationRequestAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return tuple(field.name for field in self.model._meta.fields)


@admin.register(UserSMSVerificationRecord)
class UserSMSVerificationRecordAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return tuple(field.name for field in self.model._meta.fields)
