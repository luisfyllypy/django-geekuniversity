from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContatoForm, ProdutoModelForm  # Importa o formulário criado
from .models import Produto

def index(request):
    context = {'produtos': Produto.objects.all()}

    return render(request, 'index.html', context)

def contato(request):
    # Cria uma instância do formulário (vazio ou com dados POST)
    form = ContatoForm(request.POST or None)

    # Se o metodo for POST (usuario enviou o formulário)
    if str(request.method) == 'POST':
        # Verifica se todos os campos estão válidos
        if form.is_valid():
            # Simulação de envio (apenas imprime no terminal)
            form.send_mail()

            # Mensagem de sucesso (exibida no template)
            messages.success(request, 'E-mail enviado com sucesso')

            # Recria o formulário vazio para limpar os campos
            form = ContatoForm()
        else:
            # Mensagem de erro houver-se dados inválidos. Ele irá renderizar sem apagar os dados que já foram digitados
            messages.error(request, 'Erro ao enviar e-mail')

    # Prepara o contexto com o formulário para o template
    context = {'form': form,}

    # Renderiza o template com o formulário
    return render(request, 'contato.html', context)

def produto(request):
    # Verifica se há usuario logado
    if str(request.user) != 'AnonymousUser':
        # Verifica se a requisição é do tipo POST (envio de formulário)
        if request.method == 'POST':
            # Cria uma instância do formulário com os dados e arquivos enviados
            form = ProdutoModelForm(request.POST, request.FILES)

            # Valida os dados do formulário
            if form.is_valid():
                # Salva o produto no banco de dados
                form.save()

                # Exibe mensagem de sucesso
                messages.success(request, "Produto salvo com sucesso.")

                # Recria um formulário vazio para limpar os campos
                form = ProdutoModelForm()
            else:
                # Exibe mensagem de erro se o formulário for inválido
                messages.error(request, "Error ao salvar produto")
        else:
            # Se não for POST, cria um formulário vazio (requisição GET)
            form = ProdutoModelForm()
    else:
        return redirect('index')

    # Prepara o contexto com o formulário para o template
    context = {'form': form}

    # Renderiza o template produto.html com o contexto
    return render(request, 'produto.html', context)