# Importa o módulo models do Django, que contém as classes para definir modelos de banco de dados
from django.db import models

# Define a classe Produto, que herda de models.Model
# Isso significa que Produto será uma tabela no banco de dados
class Produto(models.Model):
    # Campo 'nome' do tipo CharField (string) com:
    # - 'Nome' como rótulo para exibição
    # - max_length=100 define o tamanho máximo (100 caracteres)
    nome = models.CharField('Nome', max_length=100)

    # Campo 'preco' do tipo DecimalField (números decimais) com:
    # - 'Preço' como rótulo
    # - decimal_places=2 (2 casas decimais)
    # - max_digits=8 (8 dígitos no total, incluindo decimais)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    # Campo 'estoque' do tipo IntegerField (números inteiros)
    # - 'Quantidade em Estoque' como rótulo
    estoque = models.IntegerField('Quantidade em Estoque')

    # Metodo __str__ define como o objeto será exibido em strings
    # Quando você listar produtos no admin ou no shell, mostrará o nome
    def __str__(self):
        return self.nome

# Define a classe Cliente, outra tabela no banco de dados
class Cliente(models.Model):
    # Campo 'nome' (string com até 100 caracteres)
    nome = models.CharField('Nome', max_length=100)

    # Campo 'sobrenome' (string com até 100 caracteres)
    sobrenome = models.CharField('Sobrenome', max_length=100)

    # Campo 'email' do tipo EmailField (valida formato de e-mail)
    # - max_length=100 define o tamanho máximo
    email = models.EmailField('E-mail', max_length=100)

    # Metodo __str__ para exibir nome completo do cliente
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'