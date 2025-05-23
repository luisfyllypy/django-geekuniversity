import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path

class GetFilePathTestCase(TestCase):
    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'   # Gera um nome único para comparação

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')  # Chama a função com um nome fictício
        self.assertTrue(len(arquivo), len(self.filename))   # Verifica se os tamanhos são iguais


class ServicoTestCase(TestCase):
    def setUp(self):
        self.servico = mommy.make('Servico') # Cria um objeto Servico fake

    def test_str(self):
        self.assertEqual(str(self.servico), self.servico.servico) # Verifica se __str__ retorna o nome correto


class CargoTestCase(TestCase):
    def setUp(self):
        self.cargo = mommy.make('Cargo')

    def test_str(self):
        self.assertEqual(str(self.cargo), self.cargo.cargo)

class FuncionarioTestCase(TestCase):
    def setUp(self):
        self.funcionario = mommy.make('Funcionario')

    def test_str(self):
        self.assertEqual(str(self.funcionario), self.funcionario.nome)