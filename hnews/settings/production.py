from .base import *

DEBUG = False

import dj_database_url
DATABASES = {'default': dj_database_url.config()}

ALLOWED_HOSTS = ['https://hnews-clone.herokuapp.com/']