from django.urls import path
from . import views as v

#app_name = 'Mapa'

urlpatterns = [
    path('', v.inicio, name='inicio'),
    path('mapa/', v.MapaGeojson.as_view(), name='mapageojson'),
]
