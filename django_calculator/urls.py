"""django_calculator URL Configuration

"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from hep_app import views

from hep_app.views import create_user_view, old_math_view
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.calculate_view, name='calculate'),
    url(r'^login_view$', login, name='login_view'),
    url(r'^create_user/$', create_user_view, name='create_user_view'),
    url(r'^logout/$', logout, name='logout_view'),
    url(r'^accounts/profile/$', old_math_view, name='old_math_view'),
]
