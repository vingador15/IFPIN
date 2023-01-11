from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Sala, Turma, AdminEscola, Espaco, Produto
from Mapa.models import Local
from django.contrib.auth.models import User
from .forms import cadastrarProduto
from django.http import HttpResponseRedirect
from django.contrib import messages


@login_required
def meuPerfil(request):
    pass

@login_required
def produtos(request):

    Produtos_list = Produto.objects.all().order_by('NomeProduto')
    paginator = Paginator(Produtos_list, 18)
    page = request.GET.get('page')
    Produtos = paginator.get_page(page)
    return render(request, 'login/produtos.html', {'Produtos': Produtos})


@login_required
def produtoMeus(request):

    
    usuario = request.user
    
    Produtos_list = Produto.objects.filter(Pessoa=usuario).order_by('NomeProduto')
    
    paginator = Paginator(Produtos_list, 9)
    
    page = request.GET.get('page')
    
    Produtos = paginator.get_page(page)
    
    return render(request, 'login/produtoMeus.html', {'Produtos': Produtos})


@login_required
def produtoEditar(request, id):
    Produtos = get_object_or_404(Produto, pk=id)
    form = cadastrarProduto(instance=Produtos)

    if request.method == 'POST':
        form = cadastrarProduto(request.POST, instance=Produtos)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.Situação = 'Análise'
            produto.save()
            return redirect('produtoMeus')
        else:
            return render(request, 'login/produtoEditar.html', {'form': form, 'Produtos': Produtos})
    else:
        return render(request, 'login/produtoEditar.html', {'form': form, 'Produtos': Produtos})


@login_required
def produtoDeletar(request, id):
    Produtos = get_object_or_404(Produto, pk=id)
    Produtos.delete()
    messages.info(request, 'Produto Deletado.')
    return redirect('produtoMeus')

@login_required
def produtoCadastro(request):
    
    if request.method == 'POST':
        form = cadastrarProduto(request.POST)

        if form.is_valid():
            produto = form.save(commit=False)
            produto.Pessoa = request.user
            produto.save()
            return redirect('Produtos')
    else:
        form = cadastrarProduto()
        return render(request, 'login/produtoCadastro.html', {'form': form})


@login_required
def verProdutos(request, id):
    Produtos = get_object_or_404(Produto, pk=id)
    return render(request, 'login/verProdutos.html', {'Produtos': Produtos})


@login_required
def locais(request):

    txt_nome = request.GET.get('nome')
    if txt_nome:
        Locais = Local.objects.filter(nome__icontains=txt_nome)
    else:
        Locais = Local.objects.all()  
      
    return render(request, 'login/locais.html', {'Locais': Locais})

@login_required
def verLocal(request, id):
    Locais = get_object_or_404(Local, pk=id)
    return render(request, 'login/verLocal.html', {'Locais': Locais})


@login_required
def salas(request):

    Salas = Sala.objects.all()
    return render(request, 'login/salas.html', {'Salas': Salas})


@login_required
def verSala(request, id):
    Salas = get_object_or_404(Sala, pk=id)
    return render(request, 'login/verSala.html', {'Salas': Salas})


@login_required
def turmas(request):
    Turmas = Turma.objects.all()
    return render(request, 'login/turmas.html', {'Turmas': Turmas})


@login_required
def verTurmas(request, id):
    Turmas = get_object_or_404(Turma, pk=id)
    return render(request, 'login/verTurmas.html', {'Turmas': Turmas})


@login_required
def adminescola(request):
    AdminEscolas = AdminEscola.objects.all()
    return render(request, 'login/adminescola.html', {'AdminEscolas': AdminEscolas})


@login_required
def verAdminEscola(request, id):
    AdminEscolas = get_object_or_404(AdminEscola, pk=id)
    return render(request, 'login/verAdminEscola.html', {'AdminEscolas': AdminEscolas})


def sobre(request):
    return render(request, 'login/sobre.html')
