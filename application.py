#!/usr/bin/env python

import os

import django.core.wsgi

# When serving under WSGI (rather than runserver) use deployed config
os.environ["DJANGO_SETTINGS_MODULE"] = "config.deployed.settings"

application = django.core.wsgi.get_wsgi_application()

