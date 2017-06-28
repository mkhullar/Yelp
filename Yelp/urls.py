from django.conf.urls import url, include
from django.contrib import admin
from Charts import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^charts/', include('Charts.urls')),
]
