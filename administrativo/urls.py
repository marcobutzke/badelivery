from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('produtos/', views.produtos, name='produtos'),
    path('mercadorias/', views.mercadorias, name='mercadorias'),
    path('financeiro/', views.financeiro, name='financeiro'),
    path('resultado/', views.resultado, name='resultado'),
    path('disponibilidade/', views.disponibilidade, name='disponibilidade'),
    path('producao/', views.producao, name='producao'),
    path('consulta/', views.consulta, name='consulta')
]