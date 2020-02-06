from django.contrib import admin
from . models import signup,My_model

from django.urls import reverse
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.admin import widgets


# Register your models here.
admin.site.register(signup)
admin.site.register(My_model)





