from django.http import HttpResponse
from django.template import loader
from .models import Image

def index(request):
	imgs = Image.objects.all()
	template = loader.get_template('image/index.html')
	context={
		'imgs' : imgs
	}
	return HttpResponse(template.render(context, request))

def details(request, img_id):
	img = Image.objects.filter(id=img_id)
	template = loader.get_template('image/details.html')
	if img:
		context={
			'img' : img[0]
		}
	else:
		context={
			'img' : None
		}
	return HttpResponse(template.render(context, request))