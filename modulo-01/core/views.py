from tempfile import template
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Produto # Importa o modelo Produto do mesmo diretório

# View para a página inicial (index)
def index(request):
    # Obtém todos os produtos cadastrados no banco de dados
    produtos = Produto.objects.all()

    # Cria um dicionário de contexto com dados para o template
    context = {
        'curso': 'Programação web com Django Framework',
        'outro': 'Django é massa!',
        'produtos': produtos # Passa a lista de produtos para o template
    }
    # Renderiza o template 'index.html' com o contexto
    return render(request, 'index.html', context)

# View para a página de contato
def contato(request):
    # Renderiza o template 'contato.html' sem contexto adicional
    return render(request, 'contato.html')

# View para exibir detalhes de um produto específico
def produto(request, pk):
    # Tenta buscar um produto pelo ID ou retorna 404 se não existir
    # (alternativa comentada: Produto.objects.get(id=pk) - que levantaria exceção se não existisse)
    prod = get_object_or_404(Produto, id=pk)

    # Cria contexto contendo apenas o produto encontrado
    context = {
        'produto' : prod
    }
    # Renderiza o template 'produto.html' com os dados do produto
    return render(request, 'produto.html', context)

# View personalizada para erros 404 (página não encontrada)
def error404(request, ex):
    # Carrega o template 404.html manualmente
    template = loader.get_template('404.html')
    # Retorna uma resposta HTTP com status 404 e o template renderizado
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

# View personalizada para erros 500 (erro interno do servidor)
def error500(request):
    # Carrega o template 500.html manualmente
    template = loader.get_template('500.html')
    # Retorna uma resposta HTTP com status 500 e o template renderizado
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)