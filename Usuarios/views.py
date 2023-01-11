from django.shortcuts import render, get_object_or_404
from .forms import UsuarioForm
from .models import Perfil
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse


# Create your views here.

class UsuarioCreate(CreateView):
    template_name = 'usuarios/form2.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        
        url = super().form_valid(form)

        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url

class PerfilUpdate(UpdateView):
    template_name = 'usuarios/atualizar.html'
    model = Perfil
    fields = ['Nome', 'UltimoNome', 'TipoUsuario', 'Foto']
    success_url = reverse_lazy('verPerfil')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object

class PerfilVer(ListView):
    model = Perfil
    template_name = 'usuarios/verPerfil.html'


class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name='usuarios/alterarSenha.html'
    success_url = reverse_lazy('inicio')
