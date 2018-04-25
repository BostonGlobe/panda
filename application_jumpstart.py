#!/usr/bin/env python

import os

import django.core.wsgi

os.environ["DJANGO_SETTINGS_MODULE"] = "config.jumpstart.settings"

application = django.core.wsgi.get_wsgi_application()

