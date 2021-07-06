from django.contrib import admin
from .models import Mascotas, Vacunas

# Register your models here.

admin.site.register(Mascotas)
admin.site.register(Vacunas)