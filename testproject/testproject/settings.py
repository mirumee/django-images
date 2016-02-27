import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'a7lgs15o+%9$sj3im3)f$y^3#5eph%guxczt724o9(bh^c#rrz'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    'testapp',
    'django_images',
)

MIDDLEWARE_CLASSES = ()
ROOT_URLCONF = 'testproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'testproject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

IMAGE_AUTO_DELETE = True
IMAGE_SIZES = {
    'normal': {
        'size': (500, 0),
        'quality': 85
    },
    'tiny_square': {
        'size': (100, 100),
        'crop': True
    }
}
