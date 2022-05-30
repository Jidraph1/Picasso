from django.contrib import admin
from .models import Location, categories, Image

# Register your models here.

admin.site.register(Location)
admin.site.register(categories)
admin.site.register(Image)