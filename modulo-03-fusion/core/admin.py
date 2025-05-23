from django.contrib import admin
from .models import Cargo, Servico, Funcionario

@admin.register(Cargo)                                  # Decorador que registra a classe Cargo
class CargoAdmin(admin.ModelAdmin):                     # Configurações do admin para o modelo Cargo
    list_display = ('cargo', 'ativo', 'modificado')     # Campos exibidos na lista
# O decorador @admin.register pega a classe CargoAdmin e registra ela no painel de administração do Django para o modelo Cargo.

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')