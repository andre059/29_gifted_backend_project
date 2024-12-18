import os
from pathlib import Path
import sentry_sdk
from dotenv import load_dotenv
from yookassa import Configuration

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

sentry_sdk.init(
    dsn=os.getenv("GIFTED_29_SENTRY_DSN"),
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)
SECRET_KEY = os.environ.get("GIFTED_29_DJANGO_SECRET_KEY")
DEBUG = os.environ.get("GIFTED_29_DJANGO_DEBUG")

ALLOWED_HOSTS = [
    "0.0.0.0", "127.0.0.1",
    "localhost", "gifted-01.god-it.ru",
    "gifted-01-dev.god-it.ru", "gifted-01-test.god-it.ru",
     ]

CSRF_TRUSTED_ORIGINS = [
    "https://gifted-01.god-it.ru",
    "https://gifted-01-dev.god-it.ru", 
    "https://gifted-01-test.god-it.ru",
    "http://gifted-01.god-it.ru",
    "http://gifted-01-dev.god-it.ru", 
    "http://gifted-01-test.god-it.ru",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "http://0.0.0.0:8000",
    "https://127.0.0.1:8000",
    "https://localhost:8000",
    "https://0.0.0.0:8000",
     ]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "drf_yasg",
    "corsheaders",

    "users",
    "about_us_app",
    "assistance_form_app",
    "events_app",
    "friends_app",
    "news_app",
    "projects_app",
    "feedback_app",
    "transfer_app",
    "team",
    "contacts",

]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("GIFTED_29_DB_NAME"),
        "USER": os.environ.get("GIFTED_29_DB_USER"),
        "PASSWORD": os.environ.get("GIFTED_29_DB_PASS"),
        "HOST": os.environ.get("GIFTED_29_DB_HOST"),
        "PORT": 5432,
    }

}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "Europe/Moscow"
USE_I18N = True
USE_TZ = True
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "users.User"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema"
}

ADMIN_PASS = os.getenv("GIFTED_29_ADMIN_PASS")
ADMIN_USERNAME = os.getenv("GIFTED_29_ADMIN_USERNAME")
ADMIN_EMAIL = os.getenv("GIFTED_29_ADMIN_EMAIL")
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("GIFTED_29_EMAIL_HOST")
EMAIL_PORT = 465
EMAIL_HOST_USER = os.getenv("GIFTED_29_EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("GIFTED_29_EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_ALL_HEADERS = True
CORS_ALLOW_ALL_METHODS = True
MAX_BALANCE_DIGITS = 11
YANDEX_ACCOUNT_ID = os.getenv("GIFTED_29_YANDEX_ACCOUNT_ID")
Configuration.account_id = YANDEX_ACCOUNT_ID
YANDEX_SECRET_KEY = os.getenv("GIFTED_29_YANDEX_SECRET_KEY")
Configuration.secret_key = YANDEX_SECRET_KEY
SITE_URL = os.getenv("GIFTED_29_SITE_URL")
IMAGE_AND_DOCS_UPLOAD_SIZE = int(os.getenv("GIFTED_29_IMAGE_AND_DOCS_UPLOAD_SIZE"))
VIDEO_UPLOAD_SIZE = int(os.getenv("GIFTED_29_VIDEO_UPLOAD_SIZE"))
PHONENUMBER_DEFAULT_REGION = "RU"
REDIS = os.getenv("GIFTED_29_REDIS")
CELERY_BROKER_URL = f"redis://{REDIS}:6379"
CELERY_RESULT_BACKEND = f"redis://{REDIS}:6379"
CELERY_TASK_TRACK_STARTED = True
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "Europe/Moscow"

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
