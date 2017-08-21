from django.conf.urls import url
from django.contrib import admin
from georace import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^home/$', views.index, name='home'),
    url(r'^events/$', views.events, name='events'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^donate/$', views.donate, name='donate'),

    url(r'register/$', views.register , name='register'),
    url(r'login/$', auth_views.login, name='login'),
    url(r'logout/$', auth_views.logout, {'next_page':'/'}, name='logout'),
    url(r'^admin/', admin.site.urls),

]
