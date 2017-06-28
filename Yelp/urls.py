from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

from Charts import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^charts/', include('Charts.urls', namespace='charts')),
    url(r'^$', RedirectView.as_view(url='/charts/', permanent=True)),
]
