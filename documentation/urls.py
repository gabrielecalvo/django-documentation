from django.conf.urls import url
from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = [
    url(r'^(?P<path>.*)$', views.documentation),
]
