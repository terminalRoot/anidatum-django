from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from .models import Image


class IndexView(generic.ListView):
	template_name = 'image/index.html'
	context_object_name = 'imgs'

	def get_queryset(self):
		return Image.objects.all()

class DetailView(generic.DetailView):
	model = Image
	template_name = 'image/details.html'
	context_object_name = 'img'

class ImageCreate(CreateView):
	model = Image
	fields = ['source']
	template_name = 'image/image_form.html'