from django.conf.urls import include, url
from chicp import views

urlpatterns = [
		url(r'^$', views.chicpea, name='chicp'),
		url(r'^docs/$', views.chicpeaDocs, name='chicpeaDocs'),
		url(r'^docs/(?P<subPage>.*)/$', views.chicpeaDocs, name='chicpeaDocs'),
		url(r'^contact$', views.contactUs, name='contactUs'),
		url(r'^search(.*)$', views.chicpeaSearch, name='chicpeaSearch'),
		url(r'^subSearch(.*)$', views.chicpeaSubSearch, name='chicpeaSubSearch'),
		url(r'^fileUpload(.*)$', views.chicpeaFileUpload, name='chicpeaFileUpload'),
		url(r'^download(.*)$', views.chicpeaDownload, name='chicpeaDownload'),
		url(r'^deleteUserData(.*)$', views.chicpeaDeleteUD, name='chicpeaDeleteUD'),
		]

