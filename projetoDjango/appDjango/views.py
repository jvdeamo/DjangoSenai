from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ItemEstoqueForm, EstoqueForm
from .models import Estoque

# Create your views here.


def index(request):
    return HttpResponse('Seja bem vindo.')


def indexLoja(request):
    return render(request, 'appDjango/index.html')


def estoqueLoja(request):
    produtos = Estoque.objects.all()
    produtosForm = EstoqueForm(request.POST or None)

    if request.method == 'POST':
        if produtosForm.is_valid():
            produtosForm.save()
            produtosForm = EstoqueForm()
            return render(request, 'appDjango/lojaDoJotinha/estoque.html', {'produtos': produtos, 'produtosForm': produtosForm})
    return render(request, 'appDjango/lojaDoJotinha/estoque.html', {'produtos': produtos, 'produtosForm': produtosForm})


def adicionarEstoque(request):
    produtosForm = EstoqueForm(request.POST or None)
    if request.method == 'POST':
        if produtosForm.is_valid():
            produtosForm.save()
            produtosForm = EstoqueForm()
            return render(request, 'appDjango/lojaDoJotinha/adicionarProduto.html', {'produtosForm': produtosForm})
    return render(request, 'appDjango/lojaDoJotinha/adicionarProduto.html', {'produtosForm': produtosForm})


def infoEstoque(request, id):
    item = get_object_or_404(Estoque, id=id)  # Obtém o item com o ID fornecido
    return render(request, "appDjango/lojaDoJotinha/detalhesProduto.html", {"produto": item})



def editarEstoque(request, id):
    produto = get_object_or_404(Estoque, id=id)

    if request.method == 'POST':
        produto_form = EstoqueForm(request.POST, instance=produto)
        if produto_form.is_valid():
            produto_form.save()
            return redirect('infoEstoque', id=id)
    else:
        produto_form = EstoqueForm(instance=produto)
    return render(request, 'appDjango/lojaDoJotinha/editarProduto.html', {'produto_form': produto_form, 'produto': produto})


def excluirProduto(request, id):
    produto = get_object_or_404(Estoque, id=id)
    produto.delete()

    if request.method == 'POST':
        return redirect('estoqueLoja')
    return render(request, 'appDjango/lojaDoJotinha/excluirProduto.html', {'produto': produto})
