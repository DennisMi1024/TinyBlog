from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MyBlog',
        'USER':'root',
        'PASSWORD':'dennis',
        'HOST':'192.168.10.105',
        'PORT':'3306',
    }
}


ALLOWED_HOSTS = ['localhost', ]

MIDDLEWARE_CLASSES += (
    'middleware.profile.ProfilerMiddleware',
)
PAGE_SIZE = 4

JQUERY_URL = "https://code.jquery.com/jquery-2.1.4.min.js"


MEDIA_ROOT='/var/www/MyBlog/'
STATIC_PATH='/var/www/MyBlog/static/'
TEMPALTE_DIRS='/var/www/MyBlog/templates/'
