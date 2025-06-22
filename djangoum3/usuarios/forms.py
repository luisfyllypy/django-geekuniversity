from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUsuario

class CustomUsuarioCreateForm(UserCreationForm):
    # O email é o USERNAME_FIELD, então ele deve ser o campo 'username' do formulário
    # para UserCreationForm.
    # UserCreationForm já lida com 'password' e 'password2'.
    class Meta(UserCreationForm.Meta): # Herde de UserCreationForm.Meta
        model = CustomUsuario
        # Inclua o 'email' (que é o username_field) e os campos obrigatórios.
        # Não inclua 'password' aqui, pois UserCreationForm já o trata.
        fields = ('email', 'first_name', 'last_name', 'fone') #
        # Não precisa de labels para 'username' se 'email' já for o campo esperado.

    # Remova o metodo save() sobrescrito.
    # UserCreationForm já lida com a criação de usuário e hash de senha.
    # O UserCreationForm automaticamente pega o USERNAME_FIELD para o 'username' dele.

class CustomUsuarioChangeForm(UserChangeForm): # Deve herdar de UserChangeForm, não CustomUsuarioCreateForm
    class Meta(UserChangeForm.Meta): # Herde de UserChangeForm.Meta
        model = CustomUsuario
        # Inclua todos os campos que você deseja editar no admin, incluindo o email.
        # UserChangeForm já lida com a senha de forma segura.
        fields = ('email', 'first_name', 'last_name', 'fone', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'last_login', 'date_joined') #