from django.conf.urls import patterns, url

from django.conf import settings
from django.conf.urls.static import static

from library import views

urlpatterns = patterns('',
                    url(r'^$', views.index, name='index'),
                    url(r'^submit/$', views.submit, name='index'),
                    url(r'^submit/submit_paper$', views.submit_paper, name='index'),
                    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
