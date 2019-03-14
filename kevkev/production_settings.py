from kevkev.settings import *

PAYPAL_TEST = False
DEBUG = False

STATIC_ROOT = '/kevin_website/site/public/static'
MEDIA_ROOT = '/kevin_website/site/public/media'

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
