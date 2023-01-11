from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Local
# Register your models here.

@admin.register(Local)
class MapaAdmin(LeafletGeoAdmin):
    list_display = ['nome', 'referencia']

