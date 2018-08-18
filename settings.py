

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    ......
    # Our app
    'app',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        ....
    },
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STATIC_DIR,
]
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "static_root")


MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR # os.path.join(BASE_DIR, 'media')

# if the media folder is located out of the project's main directory
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "media_root")

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = 'home' # এই url চাইলে login function-এর ভিতরে redirect করা যায়
LOGOUT_REDIRECT_URL = 'thanks' # if we want to redirect to another page

LOGOUT_REDIRECT_URL = '/login/'
ROOT_URLCONF = 'project.urls' # Important
