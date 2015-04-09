"""
Django settings for mrtaline project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dymb&jmr%9mpnz)3$$!7!%za%77nsnuzx&7mh7vh_vh_%6%uj#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'social.apps.django_app.default',
    'materialize',
    'materializecssform',
    'crispy_forms',
    'leaflet',
    'home',
    'reports',
    'blog',
    'notes',
    'announces',
    'activities',
    'businesses',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.static',
   'django.core.context_processors.tz',
   'django.contrib.messages.context_processors.messages',
   'social.apps.django_app.context_processors.backends',
   'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'mrtaline.urls'

WSGI_APPLICATION = 'mrtaline.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'mrtaline_development',
        'USER': 'admin',
        'PASSWORD': 'bangkok',
        'HOST': 'localhost',
        'PORT': '',
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'Asia/Bangkok'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
APPEND_SLASH = True

# Set TEMPLATE_DIRS
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "static", "templates"),
)

# Set MEDIA_URL
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "static", "media")
STATIC_ROOT = os.path.join(BASE_DIR, "static", "static-only")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static", "static"),
)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder")

from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (13.736717, 100.523186),
    'DEFAULT_ZOOM': 11,
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 24,
}

# Default layout to use with "crispy_forms"
CRISPY_TEMPLATE_PACK = 'bootstrap3'

LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_FACEBOOK_KEY = '811007182285158'
SOCIAL_AUTH_FACEBOOK_SECRET = '59e64bbb88ae6386a72dbe777bd4d2d9'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '37715509319-g8tnadv6tfn64kccbgid41ha888fs9pv.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET  = 'OtiabI9oWT5TrTMUc1ZpX_Lr'

SOCIAL_AUTH_TWITTER_KEY = 'Em2P3RIwa9g7a9Ku0BYbmPY3O'
SOCIAL_AUTH_TWITTER_SECRET = 'i5h0TTZ3E4llYn013yZWy1ukwrOcyhV5Y65RvzNILqQ62kT0Ub'
