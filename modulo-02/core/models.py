from django.db import models
from stdimage.models import StdImageField   # Campo de imagem com processamento

# SIGNALS (Sinais do Django para ações pré/pós-salvamento)
from django.db.models import signals
from django.template.defaultfilters import slugify  # Para criar slugs amigáveis

class Base(models.Model):
    """
    Classe abstrata base que será herdada por outros modelos.
    Campos comuns a vários modelos podem ser definidos aqui.
    """
    criado = models.DateField('Data de Criação', auto_now_add=True) # Data automática na criação
    modificado = models.DateField('Data de Atualização', auto_now=True) # Data automática na atualização
    ativo = models.BooleanField('Ativo?', default=True) # Status do registro

    class Meta:
        abstract = True # Define que esta é uma classe abstrata (não gera tabela no BD)

class Produto(Base):
    """
    Modelo de Produto que herda da classe Base.
    Representa os produtos do sistema.
    """
    nome = models.CharField('Nome', max_length=100) # Campo de texto com no máximo 100 caracteres
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)    # Campo decimal para valores monetários
    estoque = models.IntegerField('Estoque')    # Quantidade em estoque (número inteiro)

    # Campo de imagem com redimensionamento automático:
    imagem = StdImageField(
        'Imagem',
        upload_to='produtos',   # Pasta onde as imagens serão salvas
        variations={'thumb': (124, 124)}    # Cria uma miniatura de 124x124 pixels
    )

    # Slug para URLs amigáveis (gerado automaticamente):
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        """Representação em string do produto (usado no admin e shell)"""
        return self.nome

def produto_pre_save(signal, instance, sender, **kwargs):
    """
    Função signal que é executada ANTES de salvar um Produto.
    Gera automaticamente um slug baseado no nome do produto.
    """
    instance.slug = slugify(instance.nome)  # Converte o nome para slug (ex: "Nome Produto" → "nome-produto")

# Conecta o signal pré-salvamento ao modelo Produto
signals.pre_save.connect(produto_pre_save, sender=Produto)