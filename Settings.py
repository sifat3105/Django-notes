# __________connect database_______________
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'commarce_website',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


#_______________AUTHENTICATION_BACKENDs______________

AUTHENTICATION_BACKENDs = [
    'django.countrib.auth.backends.ModelBackend'
]


#_______________static and media ____________
STATIC_URL = 'static/'
MEDIA_URL = 'media/'
STATICFILES_DIRS = [BASE_DIR / 'static', ]
MEDIA_ROOT = BASE_DIR / 'media'


#________________ Send mail _________________

EMAIL_BackEND = 'django.care.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'exmaple@gmail.com'
EMAIL_HOST_PASSWORD = 'fujf grsf fead dwdd'


#________________________ MIDDLEWARE ______________

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]


#_________*****************_____________

#        Some setting in urls



from django.urls import path
from .views import create_product, product_view, upload_and_convert_image

urlpatterns = [
    path('create_product/', create_product, name='create_product'),
    path('', product_view, name='product_view'),
    path('upload/', upload_and_convert_image, name='upload_and_convert_image'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
