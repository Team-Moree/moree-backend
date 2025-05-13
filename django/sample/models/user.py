from django.db import models
from django.utils.translation import gettext_lazy as _

from core.enums import StatusEnum
from sample.enums import UserStatusEnum, UserGenderEnum, UserProviderEnum, UserLogTypeEnum, UserStoreBookmarkVisibilityEnum, UserReviewReportReasonEnum


class User(models.Model):
    name = models.CharField(
        max_length=255,
        db_index=True
    )
    status = models.CharField(
        max_length=64,
        db_index=True,
        choices=UserStatusEnum.choices,
        default=UserStatusEnum.ACTIVE.value
    )
    email = models.EmailField(db_index=True)
    phone = models.CharField(
        max_length=64,
        db_index=True,
        null=True
    )
    gender = models.CharField(
        max_length=64,
        choices=UserGenderEnum.choices,
        db_index=True
    )
    birthday = models.DateField(
        db_index=True
    )
    profile_img_stored_file = models.ForeignKey(
        "common.StoredFile",
        on_delete=models.RESTRICT,
        db_index=True,
        null=True
    )
    profile_backgroud_img_stored_files_group = models.ForeignKey(
        "common.StoredFilesGroup",
        on_delete=models.RESTRICT,
        db_index=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}({self.email})"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class UserAccessToken(models.Model):
    user = models.OneToOneField(
        "sample.User",
        on_delete=models.CASCADE,
        db_index=True
    )
    user_refresh_token = models.OneToOneField(
        "sample.UserRefreshToken",
        on_delete=models.CASCADE,
        db_index=True
    )
    device_id = models.CharField(
        max_length=255,
        db_index=True
    )
    token = models.CharField(
        max_length=2048,
        db_index=True
    )
    expire_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("User Access Token")
        verbose_name_plural = _("User Access Tokens")


class UserRefreshToken(models.Model):
    user = models.OneToOneField(
        "sample.User",
        on_delete=models.CASCADE,
        db_index=True
    )
    device_id = models.CharField(
        max_length=255,
        db_index=True
    )
    provider = models.CharField(
        max_length=64,
        db_index=True,
        choices=UserProviderEnum.choices
    )
    provider_user_id = models.CharField(
        max_length=255
    )
    provider_token = models.CharField(
        max_length=2048,
        db_index=True
    )
    token = models.CharField(
        max_length=2048,
        db_index=True
    )
    expire_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("User Refresh Token")
        verbose_name_plural = _("User Refresh Tokens")


class UserCharacterInventory(models.Model):
    user = models.ForeignKey(
        "sample.User",
        on_delete=models.CASCADE,
        db_index=True
    )
    character = models.ForeignKey(
        "sample.Character",
        on_delete=models.CASCADE,
        db_index=True
    )
    store = models.ForeignKey(
        "sample.Store",
        on_delete=models.CASCADE,
        db_index=True,
        help_text="유저가 해당 스토어에서 뽑기를 진행한 적이 있는지 없는지 판별하기 위함"
    )
    status = models.CharField(
        max_length=64,
        choices=StatusEnum.choices,
        default=StatusEnum.ACTIVE.value,
        db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("User Character Inventory")
        verbose_name_plural = _("User Character Inventories")


class UserFolloing(models.Model):
    user = models.OneToOneField(
        "sample.User",
        on_delete=models.CASCADE,
        db_index=True
    )
    following_user = models.ForeignKey(
        "sample.User",
        on_delete=models.CASCADE,
        db_index=True,
        related_name="following_user_sets"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("User Following")
        verbose_name_plural = _("User Followings")


# class UserFeed(models.Model):
#     user = models.ForeignKey(
#         "sample.User",
#         on_delete=models.CASCADE,
#         db_index=True
#     )
#     content = models.TextField()
#     img_stored_files_group = models.ForeignKey(
#         "common.StoredFilesGroup",
#         on_delete=models.RESTRICT,
#         db_index=True,
#         default=None,
#         null=True
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name = _("User Feed")
#         verbose_name_plural = _("User Feeds")


class UserTermAgreement(models.Model):
    term = models.ForeignKey(
        "sample.Term",
        on_delete=models.RESTRICT,
        db_index=True
    )
    user = models.ForeignKey(
        "sample.User",
        on_delete=models.RESTRICT,
        db_index=True
    )
    is_agreed = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("User Term Agreement")
        verbose_name_plural = _("User Term Agreements")


class UserReview(models.Model):
    user = models.ForeignKey(
        "sample.User",
        on_delete=models.CASCADE,
        db_index=True
    )
    store = models.ForeignKey(
        "sample.Store",
        on_delete=models.CASCADE,
        db_index=True
    )
    content = models.TextField()
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        db_index=True
    )
    img_stored_files_group = models.ForeignKey(
        "common.StoredFilesGroup",
        on_delete=models.RESTRICT,
        db_index=True,
        default=None,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("User Review")
        verbose_name_plural = _("User Reviews")


class UserReviewReport(models.Model):
    user_review = models.ForeignKey(
        "sample.UserReview",
        on_delete=models.CASCADE,
        db_index=True
    )
    user = models.ForeignKey(
        "sample.User",
        on_delete=models.CASCADE,
        db_index=True
    )
    reason = models.CharField(
        max_length=64,
        choices=UserReviewReportReasonEnum.choices,
        db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("User Review Report")
        verbose_name_plural = _("User Review Reports")


class UserStoreStamp(models.Model):
    user = models.ForeignKey(
        "sample.User",
        on_delete=models.CASCADE,
        db_index=True
    )
    store = models.ForeignKey(
        "sample.Store",
        on_delete=models.CASCADE,
        db_index=True
    )
    content = models.TextField()
    img_stored_file = models.ForeignKey(
        "common.StoredFile",
        on_delete=models.RESTRICT,
        db_index=True,
        default=None,
        null=True
    )
    # img_stored_files_group = models.ForeignKey(
    #     "common.StoredFilesGroup",
    #     on_delete=models.RESTRICT,
    #     db_index=True,
    #     default=None,
    #     null=True
    # )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("User Store Stamp")
        verbose_name_plural = _("User Store Stamps")


class UserStoreBookmark(models.Model):
    user = models.ForeignKey(
        "sample.User",
        on_delete=models.CASCADE,
        db_index=True
    )
    stores = models.ManyToManyField(
        "sample.Store",
        db_index=True
    )
    title = models.CharField(
        max_length=255,
        db_index=True
    )
    description = models.TextField()
    visibility = models.CharField(
        max_length=64,
        choices=UserStoreBookmarkVisibilityEnum.choices,
        default=UserStoreBookmarkVisibilityEnum.PRIVATE.value,
        db_index=True
    )
    icon_img_stored_file = models.ForeignKey(
        "common.StoredFile",
        on_delete=models.RESTRICT,
        db_index=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("User Store Bookmark")
        verbose_name_plural = _("User Store Bookmarks")


class UserStoreCategory(models.Model):
    store_category = models.ForeignKey(
        "sample.StoreCategory",
        on_delete=models.CASCADE,
        db_index=True
    )
    user = models.ForeignKey(
        "sample.User",
        on_delete=models.CASCADE,
        db_index=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("User Store Category")
        verbose_name_plural = _("User Store Categories")


class UserLog(models.Model):
    user = models.ForeignKey(
        "sample.User",
        db_index=True,
        on_delete=models.RESTRICT
    )
    type = models.CharField(
        max_length=64,
        choices=UserLogTypeEnum.choices,
        db_index=True,
        help_text="행동 유형(회원가입, 회원탈퇴, 로그인, 로그아웃, 결제 관련 등)"
    )
    target_id = models.PositiveIntegerField(null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type}({self.user.name})"
    
    class Meta:
        verbose_name = _("User Log")
        verbose_name_plural = _("User Logs")
    

class UserSMSVerification(models.Model):
    content = models.TextField()
    status = models.CharField(
        max_length=64,
        db_index=True,
        choices=StatusEnum.choices,
        default=StatusEnum.INACTIVE.value
    )
    hash = models.CharField(
        max_length=255,
        db_index=True,
        editable=False,
        # default=lambda: hashlib.md5(binary).hexdigest()
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("User SMS Verification")
        verbose_name_plural = _("User SMS Verification")


class UserSMSVerificationRequest(models.Model):
    user_sms_verification = models.ForeignKey(
        "sample.UserSMSVerification",
        on_delete=models.RESTRICT,
        db_index=True
    )
    user = models.ForeignKey(
        "sample.User",
        on_delete=models.CASCADE,
        db_index=True
    )
    phone = models.CharField(
        max_length=64,
        db_index=True
    )
    code = models.CharField(
        max_length=6,
        db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("User SMS Verification Request")
        verbose_name_plural = _("User SMS Verification Requests")


class UserSMSVerificationRecord(models.Model):
    user = models.ForeignKey(
        "sample.User",
        on_delete=models.CASCADE,
        db_index=True
    )
    phone = models.CharField(
        max_length=64,
        db_index=True
        # unique 인 값은 아니지만 신규 등록시 기존 인증은 Inactive 혹은 deleted 해야함
    )
    status = models.CharField(
        max_length=64,
        db_index=True,
        choices=StatusEnum.choices,
        default=StatusEnum.ACTIVE.value
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("User SMS Verification Record")
        verbose_name_plural = _("User SMS Verification Records")
