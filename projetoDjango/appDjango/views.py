from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .forms import EstoqueForm
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
    produto = Estoque.objects.get(id=id)
    return render(request, 'appDjango/lojaDoJotinha/detalhesProduto.html', {'produto': produto})


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
