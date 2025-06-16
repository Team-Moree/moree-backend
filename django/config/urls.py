"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from common.views import (
    StoredFileView,
    StoredFileDetailView,
    StoredFilesGroupView,
    StoredFilesGroupDetailView
)
from moree.views import (
    UserView,
    UserDetailView,
    UserAccessTokenView,
    UserAccessTokenDetailView,
    UserRefreshTokenView,
    UserRefreshTokenDetailView,
    # UserLogView,
    # UserLogDetailView,
    UserCharacterInventoryView,
    UserCharacterInventoryDetailView,
    UserReviewView,
    UserReviewDetailView,
    UserReviewReportView,
    UserReviewReportDetailView,
    UserStoreBookmarkView,
    UserStoreBookmarkDetailView,
    UserStoreCategoryView,
    UserStoreCategoryDetailView,
    UserStoreStampView,
    UserStoreStampDetailView,
    UserTermAgreementView,
    UserTermAgreementDetailView,
    StoreView,
    StoreDetailView,
    StoreCategoryView,
    StoreCategoryDetailView,
    StoreCharacterPoolView,
    StoreCharacterPoolDetailView,
    CharacterView,
    CharacterDetailView,
    TermView,
    TermDetailView,
    TermCategoryView,
    TermCategoryDetailView
)


schema_view = get_schema_view(
    openapi.Info(
        title="Moree API",
        default_version="0.0.1",
        description="Moree API Docs",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="goct8@naver.com"),
        license=openapi.License(name="mit"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

admin.site.site_title = "Moree Admin 시스템"
admin.site.site_header = "Moree Admin 페이지"
admin.site.index_title = "Moree Admin 대시보드"

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger"),
    path('user/', UserView.as_view(), name='user'),
    path("user/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("user-access-token/", UserAccessTokenView.as_view(), name='user-access-token'),
    path("user-access-token/<int:pk>/", UserAccessTokenDetailView.as_view(), name="user-access-token-detail"),
    path("user-refresh-token/", UserRefreshTokenView.as_view(), name='user-refresh-token'),
    path("user-refresh-token/<int:pk>/", UserRefreshTokenDetailView.as_view(), name="user-refresh-token-detail"),
    # path("user-log/", UserLogView.as_view(), name='user-log'),
    # path("user-log/<int:pk>/", UserLogDetailView.as_view(), name="user-log-detail"),
    path("user-character-inventory/", UserCharacterInventoryView.as_view(), name='user-character-inventory'),
    path("user-character-inventory/<int:pk>/", UserCharacterInventoryDetailView.as_view(), name="user-character-inventory-detail"),
    path("user-review/", UserReviewView.as_view(), name='user-review'),
    path("user-review/<int:pk>/", UserReviewDetailView.as_view(), name="user-review-detail"),
    path("user-review-report/", UserReviewReportView.as_view(), name='user-review-report'),
    path("user-review-report/<int:pk>/", UserReviewReportDetailView.as_view(), name="user-review-report-detail"),
    path("user-store-bookmark/", UserStoreBookmarkView.as_view(), name='user-store-bookmark'),
    path("user-store-bookmark/<int:pk>/", UserStoreBookmarkDetailView.as_view(), name="user-store-bookmark-detail"),
    path("user-store-category/", UserStoreCategoryView.as_view(), name='user-store-category'),
    path("user-store-category/<int:pk>/", UserStoreCategoryDetailView.as_view(), name="user-store-category-detail"),
    path("user-store-stamp/", UserStoreStampView.as_view(), name='user-store-stamp'),
    path("user-store-stamp/<int:pk>/", UserStoreStampDetailView.as_view(), name="user-store-stamp-detail"),
    path("user-term-agreement/", UserTermAgreementView.as_view(), name='user-term-agreement'),
    path("user-term-agreement/<int:pk>/", UserTermAgreementDetailView.as_view(), name="user-term-agreement-detail"),
    path('stored-file/', StoredFileView.as_view(), name='stored-file'),
    path("stored-file/<int:pk>/", StoredFileDetailView.as_view(), name="stored-file-detail"),
    path('stored-files-group/', StoredFilesGroupView.as_view(), name='stored-files-group'),
    path("stored-files-group/<int:pk>/", StoredFilesGroupDetailView.as_view(), name="stored-files-group-detail"),
    path("store/", StoreView.as_view(), name='store'),
    path("store/<int:pk>/", StoreDetailView.as_view(), name='store-detail'),
    path("store-category/", StoreCategoryView.as_view(), name='store-category'),
    path("store-category/<int:pk>/", StoreCategoryDetailView.as_view(), name='store-category-detail'),
    path("store-character-pool/", StoreCharacterPoolView.as_view(), name='store-character-pool'),
    path("store-character-pool/<int:pk>/", StoreCharacterPoolDetailView.as_view(), name='store-character-pool-detail'),
    path("character/", CharacterView.as_view(), name='character'),
    path("character/<int:pk>/", CharacterDetailView.as_view(), name='character-detail'),
    path("term/", TermView.as_view(), name='term'),
    path("term/<int:pk>/", TermDetailView.as_view(), name='term-detail'),
    path("term-category/", TermCategoryView.as_view(), name='term-category'),
    path("term-category/<int:pk>/", TermCategoryDetailView.as_view(), name='term-category-detail'),
]
