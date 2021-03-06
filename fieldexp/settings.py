"""
    Django settings for fieldexp project.
    
    For more information on this file, see
    https://docs.djangoproject.com/en/1.6/topics/settings/
    
    For the full list of settings and their values, see
    https://docs.djangoproject.com/en/1.6/ref/settings/
    """

# Honor the 'X-Forwarded-Proto' header the request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b1!dx6cg6=qrrfz48m-7j5zhabtj1f@ug!%ixf#+!_nypj4433'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG


# Application definition

INSTALLED_APPS = (
                  'django.contrib.admin',
                  'django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django.contrib.messages',
                  'django.contrib.staticfiles',
                  'library',
                  'haystack'
                  )

MIDDLEWARE_CLASSES = (
                      'django.contrib.sessions.middleware.SessionMiddleware',
                      'django.middleware.common.CommonMiddleware',
                      'django.middleware.csrf.CsrfViewMiddleware',
                      'django.contrib.auth.middleware.AuthenticationMiddleware',
                      'django.contrib.messages.middleware.MessageMiddleware',
                      'django.middleware.clickjacking.XFrameOptionsMiddleware',
                      )

ROOT_URLCONF = 'fieldexp.urls'

WSGI_APPLICATION = 'fieldexp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
                    os.path.join(BASE_DIR, 'static'),
                    )

TEMPLATE_DIRS = (
                 os.path.join(BASE_DIR, 'templates'),
                 )

# Media files
MEDIA_ROOT = '/home/myusername/mypaper/' ## Change this
MEDIA_URL = '/media/'

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()