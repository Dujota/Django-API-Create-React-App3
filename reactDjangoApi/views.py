import logging
import os

from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings


class ReactAppMountingPoint(View):
    def get(self, request):
        try:
            with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            logging.exception('Production Build of App not found')
            return HttpResponse(status=501)
