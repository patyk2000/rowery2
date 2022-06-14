from itertools import product
from django.contrib import admin

from .models import Typeofbike, Parts, Bike


# Register your models here.
admin.site.register(Typeofbike)
admin.site.register(Parts)
admin.site.register(Bike)