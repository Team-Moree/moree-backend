from django.contrib import admin
from sample.models import (
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
    pass


@admin.register(UserAccessToken)
class UserAccessTokenAdmin(admin.ModelAdmin):
    pass


@admin.register(UserRefreshToken)
class UserRefreshTokenAdmin(admin.ModelAdmin):
    pass


@admin.register(UserCharacterInventory)
class UserCharacterInventoryAdmin(admin.ModelAdmin):
    pass


@admin.register(UserFolloing)
class UserFolloingAdmin(admin.ModelAdmin):
    pass


@admin.register(UserTermAgreement)
class UserTermAgreementAdmin(admin.ModelAdmin):
    pass


@admin.register(UserReview)
class UserReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(UserReviewReport)
class UserReviewReportAdmin(admin.ModelAdmin):
    pass


@admin.register(UserStoreStamp)
class UserStoreStampAdmin(admin.ModelAdmin):
    pass


@admin.register(UserStoreBookmark)
class UserStoreBookmarkAdmin(admin.ModelAdmin):
    pass


@admin.register(UserStoreCategory)
class UserStoreCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(UserLog)
class UserLogAdmin(admin.ModelAdmin):
    pass


@admin.register(UserSMSVerification)
class UserSMSVerificationAdmin(admin.ModelAdmin):
    pass


@admin.register(UserSMSVerificationRequest)
class UserSMSVerificationRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(UserSMSVerificationRecord)
class UserSMSVerificationRecordAdmin(admin.ModelAdmin):
    pass


