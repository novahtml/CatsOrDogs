from rest_framework import serializers
from main.models import Picture

class ImageSerializer(serializers)
	class Meta:
		model = Picture
		fileds = ('image')
