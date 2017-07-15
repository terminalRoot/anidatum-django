from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from annotator import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^annotate/', include('annotator.urls')),
    url(r'^images/', views.ImageList.as_view()),
    url(r'^labels/', views.LabelList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)