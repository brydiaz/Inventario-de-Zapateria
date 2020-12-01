from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Color)
admin.site.register(Talla)
admin.site.register(Zapato)
admin.site.register(ZapatoPorTallaPorColor)