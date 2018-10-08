# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views as uno

urlpatterns = [

	path('', uno.Teste.as_view(), name='teste')


]