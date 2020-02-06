from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
urlpatterns = [
  url(r'^$', views.index,name="index1"),
  url(r'^python',views.python,name='python1'),

  url(r'^download/(?P<path>.*)$', serve, {'document root': settings.MEDIA_ROOT}),

   ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)