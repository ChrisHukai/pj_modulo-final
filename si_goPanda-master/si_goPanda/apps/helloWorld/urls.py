from django.conf.urls import include, url
from django.contrib import admin

import si_goPanda.apps.helloWorld.insideHelloWorld.urls as helloWorld_urls

# import si_goPanda.apps.byeWorld.urls as byeWorld

urlpatterns = [
    url(r'^helloWorld/', include(helloWorld_urls)),
]
