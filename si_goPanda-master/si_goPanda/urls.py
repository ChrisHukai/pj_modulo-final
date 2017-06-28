from django.conf.urls import include, url
from django.contrib import admin

import si_goPanda.apps.byeWorld.urls as byeWorld_urls
import si_goPanda.apps.helloWorld.urls as helloWorld_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include(byeWorld_urls)),
    url(r'^', include(helloWorld_urls)),

]
