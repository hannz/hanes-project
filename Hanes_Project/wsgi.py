"""
WSGI config for Hanes_Project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append('/var/www/vhosts/pythonindia.com/socialpost.pythonindia.com')
sys.path.append('/var/www/vhosts/pythonindia.com/socialpost.pythonindia.com/Hanes_Project')
sys.path.append('/var/www/vhosts/pythonindia.com/socialpost.pythonindia.com/hanes_project_app')

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hanes_Project.settings")
os.environ['DJANGO_SETTINGS_MODULE'] = 'Hanes_Project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


