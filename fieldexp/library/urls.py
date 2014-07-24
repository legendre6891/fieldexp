from django.conf.urls import patterns, url

from library import views

urlpatterns = patterns('',
                    url(r'^$', views.index, name='index'),
                    url(r'^submit/$', views.submit, name='index'),
                    url(r'^submit/submit_paper$', views.submit_paper, name='index'),
                    )
