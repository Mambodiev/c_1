import os
import environ
env = environ.Env()
environ.Env.read_env()

from pathlib import Path
from django.utils.translation import gettext_lazy as _
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = ['demodjangoecom.herokuapp.com', '127.0.0.1']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.postgres',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'ckeditor',
    'ckeditor_uploader',
    'modeltranslation',
    'rosetta',
    'widget_tweaks',
    'storages',

    'cart',
    'core',
    'staff',
    'marketing',
]

 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'ecom.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT'),
        'keepalives':1,
        'keepalives_idle':130,
        'keepalives_interval':10,
        'keepalives_count':15
    }
}

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES['default'].update(db_from_env)

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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
LOGIN_REDIRECT_URL = '/'
SITE_ID = 1
CRISPY_TEMPLATE_PACK = 'bootstrap4'

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', _('English')),
    ('fr', _('French')),
]

MODELTRANSLATION_TRANSLATION_FILES = (
    'cart.translation',
    # 'core.translation',
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
    # os.path.join(BASE_DIR, 'cart/locale/'),
    # os.path.join(BASE_DIR, 'core/locale/'),
)


TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# PAYPAL_CLIENT_ID = env('PAYPAL_SANDBOX_CLIENT_ID')
# PAYPAL_SECRET_KEY = env('PAYPAL_SANDBOX_SECRET_KEY')

# STRIPE_PUBLIC_KEY = env("STRIPE_PUBLIC_KEY")
# STRIPE_SECRET_KEY = env("STRIPE_SECRET_KEY")
# STRIPE_WEBHOOK_SECRET = env("STRIPE_WEBHOOK_SECRET")

if DEBUG is False:
    SESSION_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_REDIRECT_EXEMPT = []
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    ALLOWED_HOSTS = ['www.domain.com', '127.0.0.1']
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    # PAYPAL_CLIENT_ID = env('PAYPAL_LIVE_CLIENT_ID')
    # PAYPAL_SECRET_KEY = env('PAYPAL_LIVE_SECRET_KEY')

#...
SITE_ID = 1

DJANGO_WYSIWYG_FLAVOR = "ckeditor"
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_BROWSE_SHOW_DIRS = True 
CKEDITOR_RESTRICT_BY_DATE = True
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}


AWS_S3_ACCESS_KEY_ID=env('AWS_S3_ACCESS_KEY_ID')
AWS_S3_SECRET_ACCESS_KEY=env('AWS_S3_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME=env('AWS_STORAGE_BUCKET_NAME')

AWS_S3_FILE_OVERWRITE=False
AWS_DEFAULT_ACL=None

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

DEFAULT_FILE_STORAGE='storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
