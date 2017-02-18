from django.conf.urls import patterns, url
from mail_system import views
<<<<<<< HEAD
	
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^restricted/', views.restricted, name='restricted'),		
	url(r'^logout/$' , views.user_logout, name='logout'),
	)
=======

urlpatterns = patterns('', 
    url(r'^$', views.index, name = 'index'),
    url(r'^compose/$', views.compose, name = 'compose'),
	url(r'^mail_sent/$', views.mail_sent, name = 'mail_sent'))
>>>>>>> mail_store
