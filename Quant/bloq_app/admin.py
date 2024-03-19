from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(block_model)
admin.site.register(door_model)
admin.site.register(window_model)
admin.site.register(opening_model)
admin.site.register(units_model)