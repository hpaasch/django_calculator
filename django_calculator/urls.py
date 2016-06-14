"""django_calculator URL Configuration

"""
from django.conf.urls import url
from django.contrib import admin

from hep_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.calculate_view, name='calculate')
]
