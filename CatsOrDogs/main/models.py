from os import path

from django.db import models

class Picture(models.Model):
	image = models.ImageField("Картинка", upload_to='static\\image', null=True,blank=True,)

