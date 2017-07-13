from django.conf.urls import url
from . import views

app_name = 'annotator'

urlpatterns = [
	#/annotate
	url(r'^$', views.IndexView.as_view(), name='index'),

	#/annotate/<img_id>/
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'details'),

	#/annotate/image/add
	url(r'^image/add$', views.ImageCreate.as_view(), name='image-add')
]
