"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
import sys

from pathlib import Path
from core.environment import env

sys.path.append("lib")
sys.path.append("common")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.get("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if env.get("ENVIRONMENT", "").lower() == "prod" else True

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = [
    env.get("ORIGIN", "http://localhost:8000"),
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "rest_framework",
    "drf_yasg",
    "django_filters",
    "common",
    "moree"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATE_DIR_PATH = os.path.join(BASE_DIR, "templates")
os.makedirs(TEMPLATE_DIR_PATH, exist_ok=True)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [TEMPLATE_DIR_PATH],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


DEFAULT_LOG_PATH = os.path.join(BASE_DIR, "logs", "default", "latest.log")
EXTERNAL_LOG_PATH = os.path.join(BASE_DIR, "logs", "external", "latest.log")
SQL_LOG_PATH = os.path.join(BASE_DIR, "logs", "sql", "latest.log")

LOG_DIR_PATHS = [
    os.path.dirname(DEFAULT_LOG_PATH),
    os.path.dirname(EXTERNAL_LOG_PATH),
    os.path.dirname(SQL_LOG_PATH)
]

for LOG_DIR_PATH in LOG_DIR_PATHS:
    os.makedirs(LOG_DIR_PATH, exist_ok=True)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[{asctime}]-[{levelname}]-[{module}]-[PID:{process:d}]-[{filename:s}:{lineno:d}]-[{message}]",
            "style": "{",
        },
    },
    "handlers": {
        "default": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": DEFAULT_LOG_PATH,
            "formatter": "verbose",
        },
        "external": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": EXTERNAL_LOG_PATH,
            "formatter": "verbose",
        },
        "sql": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": SQL_LOG_PATH,
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["default"],
            "level": "INFO",
            "propagate": True,
        },
        "external": {
            "handlers": ["external"],
            "level": "INFO",
            "propagate": True,
        },
        "django.db.backends": {
            "handlers": ["sql"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = "ko-kr"

# TIME_ZONE = 'UTC'
TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "/django-admin/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

os.makedirs(STATIC_ROOT, exist_ok=True)

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
