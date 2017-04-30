from django.conf.urls import patterns, url
from mail_system import views

	
urlpatterns = patterns('',
	url(r'^register/$', views.user_registration, name='user_registration'),
	url(r'^login/$', views.user_login, name='login'),	
	url(r'^compose/$', views.compose_mail, name = 'compose_mail'),
	url(r'^mail_sent/$', views.send_mail, name = 'send_mail'),
	url(r'^spam/$', views.spam_mails, name = 'spam_mails'),
    url(r'^spam/move_to_inbox/', views.move_to_inbox, name = 'move_to_inbox'),
	url(r'^inbox/move_to_spam/$', views.move_to_spam, name = 'move_to_spam'),
	url(r'^inbox/$', views.inbox, name = 'inbox')
)
