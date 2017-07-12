from django.conf.urls import url
from . import views

app_name = 'annotator'

urlpatterns = [
	url(r'^$', views.index, name='index'),

	#/annotate/<img_id>/
	url(r'^(?P<img_id>[0-9]+)/$', views.details, name = 'details'),

	#/annotate/<img_id>/lable
	url(r'^(?P<img_id>[0-9]+)/label/$', views.label, name = 'label'),
]
