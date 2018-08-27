from django.conf.urls import url
from . import views

app_name = 'homepage'

# matthewmcleod.net
urlpatterns = [
    url(r'^$', views.index, name="index")
]
