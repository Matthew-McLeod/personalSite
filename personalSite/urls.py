from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns= [
    url(r'^', include('homepage.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^resume/', include('resume.urls')),
    url(r'^portfolio/', include('portfolio.urls')),
    url(r'^contact/', include('contact.urls'))
]