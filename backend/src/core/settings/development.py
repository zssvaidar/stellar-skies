from .base import *

DEBUG = True

ALLOWED_HOSTS = [
]

INSTALLED_APPS += [
    'default_home_1',
    'default_home_1_api',
    # 'debug_toolbar',
    'debug_toolbar.apps.DebugToolbarConfig',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
}

INTERNAL_IPS = [
    "127.0.0.1",
]

def show_toolbar(request):                                     # <-- NEW
    return True                                                # <-- NEW 

DEBUG_TOOLBAR_CONFIG = {                                       # <-- NEW
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar,                    # <-- NEW
}  

if DEBUG:                                                      # <-- NEW
    import mimetypes                                           # <-- NEW          
    mimetypes.add_type("application/javascript", ".js", True)  # <-- NEW
   
TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'apps/default_home_1/templates/'),
]
print(TEMPLATE_DIRS)