DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'lhc.erzat.dulat@gmail.com'
EMAIL_HOST_PASSWORD = 'qwerty181095'
EMAIL_PORT = 587
SITE_ID = 1
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(BASE_DIR, 'src', 'db.sqlite3'),                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

ALLOWED_HOSTS = []

MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static-only')

STATIC_URL = '/static/'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'static', 'templates'),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    #'django.contrib.admindocs',
    'south',
    'stripe',
    'registration',
    'banks',
    'loans',
)

ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_REDIRECT_URL = '/'

LANGUAGE_CODE = 'ru-RU'
USE_I18N = True
