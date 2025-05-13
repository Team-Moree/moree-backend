from django.db.models import TextChoices


class UserStatusEnum(TextChoices):
    ACTIVE = "ACTIVE", "Active"
    DORMANT = "DORMANT", "Dormant"
    WITHDRAWN = "WITHDRAWN", "Withdrawn"


class UserGenderEnum(TextChoices):
    MALE = "MALE", "Male"
    FEMALE = "FEMALE", "Female"


class UserProviderEnum(TextChoices):
    APPLE = "APPLE", "Apple"
    GOOGLE = "GOOGLE", "Google"


class UserLogTypeEnum(TextChoices):
    LOGIN = "LOGIN", "Login"
    LOGOUT = "LOGOUT", "Logout"
    SIGNUP = "SIGNUP", "SignUp"
    WITHDRAWAL = "WITHDRAWAL", "Withdrawal"


class UserStoreBookmarkVisibilityEnum(TextChoices):
    PUBLIC = "PUBLIC", "Public"
    FRIENDS_ONLY = "FRIENDS_ONLY", "Friends Only"
    PRIVATE = "PRIVATE", "Private"


class UserReviewReportReasonEnum(TextChoices):
    SPAM = "SPAM", "Spam"
    SCAM = "SCAM", "Scam"
    ABUSE = "ABUSE", "Abuse"
    HARASSMENT = "HARASSMENT", "Harassment"
    INAPPROPRIATE_CONTENT = "INAPPROPRIATE_CONTENT", "Inappropriate Content"
    MISINFORMATION = "MISINFORMATION", "Misinformation"
    OTHER = "OTHER", "Other"
