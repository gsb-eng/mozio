from mozio.settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('DBNAME', 'test'),
        'USER': os.environ.get('USERNAME', 'test'),
        'PASSWORD': os.environ.get('PASSWORD', ''),
        'HOST': os.environ.get('HOSTNAME', 'localhost'),
        'PORT': os.environ.get('PORT', '5432'),
    }
}
