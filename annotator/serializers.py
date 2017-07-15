from rest_framework import serializers
from .models import Image
from .models import Label
from .models import Attribute

class ImageSerializer(serializers.ModelSerializer):

	class Meta:
		model = Image
		fields = '__all__'

class LabelSerializer(serializers.ModelSerializer):

	class Meta:
		model = Label
		fields = ('img', 'attribute', 'position')
		#fields = '__all__'