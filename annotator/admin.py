# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Image
from .models import Label
from .models import Category
from .models import Attribute

# Register your models here.
admin.site.register(Image)
admin.site.register(Label)
admin.site.register(Category)
admin.site.register(Attribute)