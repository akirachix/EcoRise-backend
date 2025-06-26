from django.contrib import admin

# Register your models here.
from .models import Material,Product
admin.site.register(Product)
admin.site.register(Material)
