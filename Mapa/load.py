import os
from .models import Local
from django.contrib.gis.utils import LayerMapping

# Auto-generated `LayerMapping` dictionary for Local model
local_mapping = {
    'nome': 'Nome',
    'referencia': 'Referencia',
    'geom': 'MULTIPOINT25D',
}

shp = os.path.abspath(os.path.join('data', 'Mapa-Pontos.shp'))

def run_locais(verbose=True):
    lm = LayerMapping(Local, shp, local_mapping)
    lm.save(strict=True, verbose=True)