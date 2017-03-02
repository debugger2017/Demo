from django.conf.urls import patterns, url
from mail_system import views

	
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^restricted/', views.restricted, name='restricted'),		
	url(r'^logout/$' , views.user_logout, name='logout'),
	url(r'^compose/$', views.compose, name = 'compose'),
	url(r'^mail_sent/$', views.mail_sent, name = 'mail_sent'),
	url(r'^inbox/$', views.inbox, name = 'inbox'),
	url(r'^training/$', views.training, name = 'training'),
	url(r'^spam/$', views.spam, name = 'spam')
	)
