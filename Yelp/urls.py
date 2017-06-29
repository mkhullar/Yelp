from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

from Charts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^charts/', include('Charts.urls', namespace='charts')),
    url(r'^preloader/', views.preloader, name='preloader'),
    url(r'^$', RedirectView.as_view(url='/preloader/', permanent=True)),
]
