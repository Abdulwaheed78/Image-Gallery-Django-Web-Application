from django.contrib import admin
from .models import Imager
# Register your models here.



@admin.register(Imager)
class ImagerAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'image','date')