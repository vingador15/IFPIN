from django.urls import path
from . import views

#app_name = 'Login'

urlpatterns = [
    path('meuperfil', views.meuPerfil, name='meuPerfil'),
    path('produtos', views.produtos, name='Produtos'),
    path('produtos/meusprodutos', views.produtoMeus, name='produtoMeus'),
    path('produtos/meusprodutos/editarproduto_<int:id>', views.produtoEditar, name='produtoEditar'),
    path('produtos/meusprodutos/deletarproduto_<int:id>', views.produtoDeletar, name='produtoDeletar'),
    path('produtos/cadastro', views.produtoCadastro, name='produtoCadastro'),
    path('produtos/<int:id>', views.verProdutos, name='verProdutos'),
    path('locais', views.locais, name='Locais'),
    path('locais/<int:id>', views.verLocal, name='verLocal'),
    path('salas', views.salas, name='Salas'),
    path('salas/<int:id>', views.verSala, name='verSala'),
    path('turmas', views.turmas, name='Turmas'),
    path('turmas/<int:id>', views.verTurmas, name='verTurmas'),
    path('adminescola', views.adminescola, name='AdminEscola'),
    path('adminescola/<int:id>', views.verAdminEscola, name='verAdminEscola'),
    path('sobre', views.sobre, name='Sobre'),
]