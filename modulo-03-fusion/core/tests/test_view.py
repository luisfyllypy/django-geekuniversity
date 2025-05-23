from django.test import TestCase, Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.dados = {
            'nome': 'Mario Bros',
            'email': 'mario@nintendo.com',
            'assunto': 'Novo jogo',
            'mensagem': 'Não campactuamos com pirataria'
        }
        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEqual(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome': 'Mario Bros',
            'email': 'mario@nintendo.com',
        }
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEqual(request.status_code, 200)