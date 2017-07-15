from django.conf.urls import url
from . import views


app_name = 'annotator'

urlpatterns = [
	#/annotate
	url(r'^$', views.IndexView.as_view(), name='index'),

	#/annotate/register
	url(r'^register/$', views.UserFormView.as_view(), name='register'),

	#/annotate/<img_id>/
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'details'),

	#/annotate/image/add
	url(r'^image/add$', views.ImageCreate.as_view(), name='image-add'),

	#/annotate/image/<id>
	url(r'^image/(?P<pk>[0-9]+)/$', views.ImageUpdate.as_view(), name='image-update'),

	#/annotate/image/<id>/delete
	url(r'^image/(?P<pk>[0-9]+)/delete/$', views.ImageDelete.as_view(), name='image-delete'),
]
