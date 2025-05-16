from django import forms    # Importa o módulo de formulários do Django
from django.core.mail.message import EmailMessage
from .models import Produto

# Cria uma classe de formulário que herda de forms.Form
class ContatoForm(forms.Form):
    # Campo de texto para nome com label personalizado
    nome = forms.CharField(label='Nome')

    # Campo de e-mail com validação automática de formato
    email = forms.EmailField(label='E-mail')

    # Campo de texto para assunto
    assunto = forms.CharField(label='Assunto')

    # Campo de texto longo (textarea) para mensagem
    mensagem = forms.CharField(
        label='mensagem',
        widget=forms.Textarea   # Altera o widget padrão para Textarea
    )

    # Metodo personalizado para enviar e-mail com os dados do formulário
    def send_mail(self):
        # Extrai os dados validados do formulário
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']
        # Formata o conteúdo do e-mail com os dados
        conteudo = (f'Nome: {nome}\n'
                    f'E-mail: {email}\n'
                    f'Assunto: {assunto}\n'
                    f'Mensagem {mensagem}')

        # Cria objeto de e-mail do Django
        mail = EmailMessage(
            subject='E-mail enviado pelo sistema django2', # Assunto fixo + poderia incluir o assunto do formulário
            body=conteudo, # Corpo formatado
            from_email='contato@teste.com', # E-mail remetente (deveria vir das settings)
            to=['contato@teste.com'], # Lista de destinatários (deveria ser configurável)
            headers={'Reply-To': email} # Permite resposta direta para quem preencheu o formulário
        )

        # Envia o e-mail de fato
        mail.send()

# Define um ModelForm baseado no modelo Produto
class ProdutoModelForm(forms.ModelForm):
    class Meta:
        # Especifica o modelo que será usado
        model = Produto

        # Define quais campos do modelo aparecerão no formulário
        fields = ['nome', 'preco', 'estoque', 'imagem']
        # Obs: 'imagem' será um campo de upload de arquivo