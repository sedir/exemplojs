from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^listar$', views.listar_json),
    url(r'^novo$', views.novo),
]