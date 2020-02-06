

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from shortcuts.utils import render_to_pdf
from django.conf import settings
from django.http import Http404
import os
from filetransfers.api import prepare_upload
from filetransfers.api import serve_file
from django.urls import reverse
from importlib import import_module
from django.forms import forms
# Create your views here.
def index(request):
    return render(request,'app/index.html')
def python(request):
    return render(request,'app/python.html')
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


