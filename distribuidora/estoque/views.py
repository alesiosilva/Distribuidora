from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.template import loader
# from django.http import Http404
# from django.http import HttpResponse
from .models import Produto, Estoque
from .forms import *

# Views para PRODUTO.
# URL: /produto/
def product(request):
    produtos = Produto.objects.order_by('-entry_date')

    # Criação do objeto no contexto
    context = {'produtos': produtos}

    # Captura do template com o loader
    template = loader.get_template('produto/product.html')

    # Renderização do template usando httpresponse
    # return HttpResponse(template.render(context, request))

    # Renderização do template usando atalho render diretamente no html
    return render(request, 'produto/product.html', context)

# URL: /produto/<int:produto_id>/
def detail(request, produto_id):
    # Levantando erro 404 
    #try:
    #    produto = Produto.objects.get(pk=produto_id)
    #except Produto.DoesNotExist:
    #    raise Http404('Produto não existe')
    
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'produto/detail.html', {'produto': produto})

# URL: /produto/edit/<int:produto_id>/
def edit(request, produto_id):
    return render(request, 'produto/edit.html')

# URL: /produto/novo/
def register(request):
    template = 'produto/register.html'
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        produto = Produto.objects.get(pk=request.POST['produto'])
        form.save()
        form = ProdutoForm()
        messages.success(request, 'Produto cadastrado com sucesso!')
        return render(request, template, {'form': form})

    return render(request, template, {'form': form})

# Views para ESTOQUE
# URL: /estoque/
def index(request):
    estoque = Estoque.objects.order_by('-entry_date')
    context = {'estoque': estoque}
    return render(request, 'estoque/index.html', context)
   
# URL: /estoque/entrada/
def entry(request):
    return render(request, 'estoque/entry.html')

# URL: /estoque/saida/
def output(request):
    return render(request, 'estoque/output.html')