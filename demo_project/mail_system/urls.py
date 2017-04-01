from django.conf.urls import patterns, url
from mail_system import views

	
urlpatterns = patterns('',
	url(r'^register/$', views.user_register, name='user_register'),
	url(r'^login/$', views.user_login, name='login'),	
	url(r'^compose/$', views.mail_compose, name = 'mail_compose'),
	url(r'^mail_sent/$', views.mail_sent, name = 'mail_sent'),
	url(r'^spam/$', views.spam, name = 'spam'),
	url(r'^inbox/test/$', views.test, name = 'test')
)
