from django import forms
from .models import Produto

class cadastrarProduto(forms.ModelForm):

    
    class Meta:
        model = Produto
        fields = ['Lugar', 'Salas', 'NomeProduto', 'NomePessoa', 'Valor']
