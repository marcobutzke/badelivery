from django.shortcuts import render
from .charting import chart_example


def index(request):
    context = {'chart_html': chart_example()}
    return render(request=request, template_name='index.html', context=context)

def clientes(request):
    context = {}
    return render(request=request, template_name='clientes.html', context=context)

def produtos(request):
    context = {}
    return render(request=request, template_name='produtos.html', context=context)

def entregas(request):
    context = {}
    return render(request=request, template_name='entregas.html', context=context)

def financeiro(request):
    context = {}
    return render(request=request, template_name='financeiro.html', context=context)

def resultado(request):
    context = {}
    return render(request=request, template_name='resultado.html', context=context)

def producao(request):
    context = {}
    return render(request=request, template_name='producao.html', context=context)

def consulta(request):
    context = {}
    return render(request=request, template_name='consulta.html', context=context)
