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
    StoreView,
    StoreDetailView,
    StoreCategoryView,
    StoreCategoryDetailView,
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
    path('stored-file/', StoredFileView.as_view(), name='stored-file'),
    path("stored-file/<int:pk>/", StoredFileDetailView.as_view(), name="stored-file-detail"),
    path('stored-files-group/', StoredFilesGroupView.as_view(), name='stored-files-group'),
    path("stored-files-group/<int:pk>/", StoredFilesGroupDetailView.as_view(), name="stored-files-group-detail"),
    path("store", StoreView.as_view(), name='store'),
    path("store/<int:pk>/", StoreDetailView.as_view(), name='store-detail'),
    path("store-category/", StoreCategoryView.as_view(), name='store-category'),
    path("store-category/<int:pk>/", StoreCategoryDetailView.as_view(), name='store-category-detail'),
]
