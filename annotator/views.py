from django.shortcuts import render, get_object_or_404
from .models import Image, Label


def index(request):
	imgs = Image.objects.all()
	context={'imgs' : imgs}
	return render(request, 'image/index.html', context)

def details(request, img_id):
	img = get_object_or_404(Image, id=img_id)	
	return render(request, 'image/details.html', {'img' : img})

def label(request, img_id):
	img = get_object_or_404(Image, id=img_id)
	try:
		print(request.POST['label'])
		label = img.label_set.get(id=request.POST['label'])
	except (KeyError, Label.DoesNotExist):
		return render(request, 'image/details.html', {
			'img' : img,
			'err_msg' : 'Invalid input'
			})
	else:
		##update label
		#label.<<field>> = value
		#label.save()
		return render(request, 'image/details.html', {'img':img})