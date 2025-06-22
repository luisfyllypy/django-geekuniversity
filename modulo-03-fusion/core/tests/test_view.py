from django.test import TestCase, Client    # Importa a classe base de teste e um cliente HTTP para simular requisições
from django.urls import reverse_lazy    # Importa uma função que gera URLs a partir do nome da rota

class IndexViewTestCase(TestCase):
    def setUp(self):    # setUp() é executado antes de cada teste individual
        self.dados = {  # self.dados: simula os dados de um formulário corretamente preenchido
            'nome': 'Mario Bros',
            'email': 'mario@nintendo.com',
            'assunto': 'Novo jogo',
            'mensagem': 'Não campactuamos com pirataria'
        }
        self.cliente = Client() # Cria uma instância de Client, que permite simular requisições HTTP como um navegador

    def test_form_valid(self):  # Faz uma requisição POST para a URL da view 'index', passando os dados válidos
        request = self.cliente.post(reverse_lazy('index'), data=self.dados) # reverse_lazy('index'): obtém a URL correspondente ao nome da view
        self.assertEqual(request.status_code, 302)  # Espera que o status da resposta seja 302 — isso indica que a view redirecionou após o formulário ser enviado com sucesso

    def test_form_invalid(self):
        dados = {
            'nome': 'Mario Bros',
            'email': 'mario@nintendo.com',
        }
        request = self.cliente.post(reverse_lazy('index'), data=dados)  # Aqui estamos simulando o envio de um formulário incompleto, faltando os campos 'assunto' e 'mensagem'
        self.assertEqual(request.status_code, 200)  # A resposta esperada tem status 200, o que significa que o formulário não foi aceito e a página foi recarregada com erros de validação