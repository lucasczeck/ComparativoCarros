from django.urls import path, include
from comparativo import views

urlpatterns = [
    path('', views.Comparar.as_view(), name='comparativo'),
    path('comparar', views.Comparacao.as_view(), name='comparar'),
    path('cadastrar', views.CadastrarCarro.as_view(), name='cadastrar_carro')
]
