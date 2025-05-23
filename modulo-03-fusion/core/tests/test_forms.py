from django.test import TestCase
from core.forms import ContatoForm

class ContatoFormTestCase(TestCase):
    # Metodo que executa antes de cada teste
    def setUp(self):
        # Dados de exemplo para popular o formulário
        self.nome = "Murilo Antonio"
        self.email = 'mumurilo@email.com'
        self.assunto = 'Quero tirar dúvidas'
        self.mensagem = 'Exemplo de mensagem'

        # Agrupa todos os campos em um dicionário, simulando dados enviados via POST
        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }

        # Instancia o formulário com os dados de teste
        self.form = ContatoForm(data=self.dados)

    def test_send_email(self):
        # Cria uma nova instância de formulário e valida os dados
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()    # Chama a validação do Django (limpeza de dados e checagem de regras)
        res1 = form1.send_mail()    # Executa o metodo customizado send_mail e captura o resultado

        # Reutiliza a instância criada no setUp
        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        # Verifica se o retorno de ambos os envios de email é igual
        self.assertEqual(res1, res2)    # Asserção garante consistência do metodo send_mail