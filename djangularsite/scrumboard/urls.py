from django.conf.urls import url, re_path
from django.urls import path
from .api import ListApi, CardApi

urlpatterns = [
    re_path(r'^lists/$', ListApi.as_view()),
    url(r'^cards/$', CardApi.as_view())
]