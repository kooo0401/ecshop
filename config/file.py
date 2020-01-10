import os

BASE_DIR = os.path.dirname(os.path.abspath('__file__'))
print("BASE_DIR : {}".format(BASE_DIR))

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
print("STATIC_ROOT : {}".format(STATIC_ROOT))
STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
        )
print('STATICFILES_DIRS : {}'.format(STATICFILES_DIRS))
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')
print('MEDIA_ROOT : {}'.format(MEDIA_ROOT))