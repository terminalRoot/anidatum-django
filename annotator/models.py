# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Image(models.Model):
	source = models.CharField(max_length=1000)

	def __str__(self):
		return  str(self.id)+ " " +self.source


class Category(models.Model):
	name = models.CharField(max_length=256)

	def __str__(self):
		return self.name


class Attribute(models.Model):
	cat = models.ForeignKey(Category, on_delete=models.CASCADE)
	name = models.CharField(max_length=256)
	value = models.CharField(max_length=256)

	def __str__(self):
		return str(self.cat) + " " + self.name + " " + self.value
		

class Label(models.Model):
	img = models.ForeignKey(Image, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
	position = models.CharField(max_length=1000)

	def __str__(self):
		return str(self.img) + " " + str(self.category) + " " + str(self.attribute) +" " + self.position

