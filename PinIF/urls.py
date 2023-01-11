from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("Login.urls")),
    path('admin/', admin.site.urls),
    path('', include("Usuarios.urls")),
    path('', include("Mapa.urls")),
    path('chaining', include("smart_selects.urls")),
]
