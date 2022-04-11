# from whitenoise import WhiteNoise
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gu_global.settings')
application = get_wsgi_application()

# application = WhiteNoise(application, root='/web/gu_global')
# application.add_files('/web/gu_global/static/', prefix='')