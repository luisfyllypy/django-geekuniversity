from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm
from .models import CustomUsuario

@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('first_name', 'last_name', 'email', 'fone', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}), # 'email' é seu USERNAME_FIELD
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'fone')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')})
    )
    # Certifique-se de que o add_fieldsets está correto para a adição de usuários
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password2') # UserCreationForm precisa de password e password2
        }),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'fone')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )