from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^register$', views.UserFormView.as_view(), name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^login/$', login, {'template_name':'accounts/login.html'}),
]