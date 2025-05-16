from django.urls import path

from .views import index, contato, produto  # Importa as views do app

urlpatterns = [
    path('', index, name='index'),  # Rota raiz (localhost/)
    path('contato', contato, name='contato'),   # localhost/contato
    path('produto/<int:pk>', produto, name='produto')   # localhost/produto/1
]