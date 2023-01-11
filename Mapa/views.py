from django.shortcuts import render
from .models import Local
from djgeojson.views import GeoJSONLayerView


# Create your views here.
def inicio(request):
    return render(request, 'Mapa/inicio.html')

class MapaGeojson(GeoJSONLayerView):
    model = Local
    properties = ('popup_content',)


    