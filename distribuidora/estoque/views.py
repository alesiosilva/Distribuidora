# from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
# from django.http import HttpResponse
from .models import Produto, Estoque

# Create your views here.
def index(request):
    produtos = Produto.objects.order_by('-entry_date')

    # Criação do objeto no contexto
    context = {'produtos': produtos}

    # Captura do template com o loader
    template = loader.get_template('estoque/index.html')

    # Renderização do template usando httpresponse
    # return HttpResponse(template.render(context, request))

    # Renderização do template usando atalho render
    return render(request, 'estoque/index.html', context)
 
def detail(request, produto_id):
    # Levantando erro 404 
    #try:
    #    produto = Produto.objects.get(pk=produto_id)
    #except Produto.DoesNotExist:
    #    raise Http404('Produto não existe')
    
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'estoque/detail.html', {'produto': produto})
