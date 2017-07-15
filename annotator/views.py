from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators	import login_required
from django.views import generic
from django.views.generic import View
from .models import Image
from .models import Label
from .forms import UserForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LabelSerializer
from .serializers import ImageSerializer



class IndexView(generic.ListView):
	template_name = 'image/index.html'
	context_object_name = 'imgs'

	# @login_required
	def get_queryset(self):
		return Image.objects.all()

class DetailView(generic.DetailView):
	model = Image
	template_name = 'image/details.html'
	context_object_name = 'img'

class ImageCreate(CreateView):
	model = Image
	fields = ['source', 'file']
	template_name = 'image/image_form.html'

class ImageUpdate(UpdateView):
	model = Image
	fields = ['source', 'file']
	context_object_name = 'img'
	template_name = 'image/image_form.html'

class ImageDelete(DeleteView):
	model = Image
	success_url = reverse_lazy('annotator:index')

class UserFormView(View):
	form_class = UserForm
	template_name = 'image/registration_form.html'


	# display blank form
	def get(self, request):
		form = self.form_class
		return render(request, self.template_name,  {'form':form})

	# process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			# cleaned (normalize) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user.set_password(password)
			user.save()

			# returns User objects if credentials are correct
			user = authenticate(username=username, password=password)

			if user is not None:
				if user.is_active:
					print('login success')
					login(request, user)
					return redirect('annotator:index')

		return render(request, self.template_name, {'form':form})



# List all images or create new one

class ImageList(APIView):

	def get(self, request):
		images = Image.objects.all()
		#convert to JSON
		serializer = ImageSerializer(images, many=True)
		return Response(serializer.data)

	def post(self, request):
		pass

class LabelList(APIView):

	def get(self, request):
		labels = Label.objects.all()
		serializer = LabelSerializer(labels, many=True)
		return Response(serializer.data)



