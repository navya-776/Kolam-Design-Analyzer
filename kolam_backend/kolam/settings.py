"""
Django settings for kolam project.
"""

from pathlib import Path
import firebase_admin
from firebase_admin import credentials
from dotenv import load_dotenv
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
load_dotenv()

API_KEY = os.getenv("API_KEY")

CLOUDINARY = {
    'cloud_name': os.getenv('CLOUDINARY_CLOUD_NAME'),
    'api_key': os.getenv('CLOUDINARY_API_KEY'),
    'api_secret': os.getenv('CLOUDINARY_API_SECRET')
}

cloudinary.config(**CLOUDINARY)

DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10 MB limit (increase if needed)


BASE_DIR = Path(__file__).resolve().parent.parent

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cred_path = os.path.join(BASE_DIR, "firebase-key.json")

if os.path.exists(cred_path):
    cred = credentials.Certificate(cred_path)
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred)
# --------------------------
# Base directory
# --------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------
# Quick-start development settings
# --------------------------
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-fallback-key')
DEBUG = True
ALLOWED_HOSTS = [
    "kolam-design-analyzer.onrender.com",
]

# --------------------------
# Application definition
# --------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'core',
    'corsheaders',  # if you installed django-cors-headers
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',           # if CORS installed
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --------------------------
# CORS configuration
# --------------------------
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # frontend dev server
]

# --------------------------
# URL configuration
# --------------------------
ROOT_URLCONF = 'kolam.urls'

# --------------------------
# Templates
# --------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'front_end' / 'templates'],  # <-- include your template folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'kolam.context_processors.firebase_config',
            ],
        },
    },
]


# --------------------------
# WSGI
# --------------------------
WSGI_APPLICATION = 'kolam.wsgi.application'

# --------------------------
# Database
# --------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # use Path object
    }
}

# --------------------------
# Password validation
# --------------------------
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

# --------------------------
# Internationalization
# --------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --------------------------
# Static files
# --------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'front_end' /'static',  # your static folder
]

# --------------------------
# Default primary key field type
# --------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --------------------------
# Django REST Framework & JWT
# --------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
