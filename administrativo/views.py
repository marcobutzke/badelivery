from django.shortcuts import render
from django.db.models import Sum
from .charting import (
    chart_tipo_cliente,
    chart_tipo_categoria,
    chart_categoria_tipo,
    chart_rfpm,
    chart_pca,
    chart_curva_abc,
    chart_categoria_produto,
    chart_resultado_geral,
    chart_resultado_atual,
    chart_resultado_geral_atual,
    chart_financeiro_operacao,
    chart_inicio_economico,
    chart_inicio_financeiro,

)
from .models import (
    VendasPeriodoAtual,
    ReceberPeriodoAtual,
    IndicadoresEstoque,
    IndicadoresCompra,
    ResultadoAtual,
    FinanceiroReceber,
    FinanceiroPagar,
    DisponibilidadeCaixa,
    DisponibilidadeBanco,
    DisponibilidadeCartao,
    InicioEconomico,
    InicioFinanceiro,
    Periodo
)


def index(request):
    vendas = InicioEconomico.objects.filter(tipo='Venda').aggregate(total=Sum('valor'))
    compras = InicioEconomico.objects.filter(tipo='Compra').aggregate(total=Sum('valor'))
    economico = InicioEconomico.objects.all().aggregate(total=Sum('valor'))
    recebidos = InicioFinanceiro.objects.filter(tipo='Recebido').aggregate(total=Sum('valor'))
    pagos = InicioFinanceiro.objects.filter(tipo='Pago').aggregate(total=Sum('valor'))
    financeiro = InicioFinanceiro.objects.all().aggregate(total=Sum('valor'))
    referencia = Periodo.objects.filter(situacao='ATUAL').values('sigla').first()
    context = {
        'chart_inicio_economico': chart_inicio_economico(),
        'chart_inicio_financeiro': chart_inicio_financeiro(),
        'vendas': vendas,
        'compras': compras,
        'recebidos': recebidos,
        'pagos': pagos,
        'economico': economico,
        'financeiro': financeiro,
        'referencia': referencia
    }
    return render(request=request, template_name='index.html', context=context)

def clientes(request):
    total = VendasPeriodoAtual.objects.aggregate(total=Sum('valor'))
    pago = VendasPeriodoAtual.objects.filter(situacao='PAGO').values('valor').first()
    fechado = VendasPeriodoAtual.objects.filter(situacao='FECHADO').values('valor').first()
    aberto = ReceberPeriodoAtual.objects.all().values('aberto').first()
    inadimplencia = ReceberPeriodoAtual.objects.all().values('inadimplencia').first()
    referencia = Periodo.objects.filter(situacao='ATUAL').values('sigla').first()
    context = {
        'total': total,
        'pago': pago,
        'fechado': fechado,
        'aberto': aberto,
        'inadimplencia': inadimplencia,
        'chart_tipo_cliente': chart_tipo_cliente(),
        'chart_tipo_categoria': chart_tipo_categoria(),
        'chart_categoria_tipo': chart_categoria_tipo(),
        'chart_rfpm': chart_rfpm(),
        'chart_pca': chart_pca(),
        'referencia': referencia
    }
    return render(
        request=request,
        template_name='clientes.html',
        context=context
    )

def produtos(request):
    total = IndicadoresEstoque.objects.aggregate(total=Sum('saldo'))
    materiaprima = IndicadoresEstoque.objects.filter(conta='Estoque Matéria-Prima').values('saldo').first()
    produto = IndicadoresEstoque.objects.filter(conta='Estoque Produto').values('saldo').first()
    acessorio = IndicadoresEstoque.objects.filter(conta='Estoque Acessório').values('saldo').first()
    referencia = Periodo.objects.filter(situacao='ATUAL').values('sigla').first()
    context = {
        'total': total,
        'materiaprima': materiaprima,
        'produto': produto,
        'acessorio': acessorio,
        'chart_curva_abc': chart_curva_abc(),
        'chart_categoria_produto': chart_categoria_produto(),
        'referencia': referencia
    }
    return render(
        request=request,
        template_name='produtos.html',
        context=context
    )

def mercadorias(request):
    compras_mes = IndicadoresCompra.objects.all().values('compras_mes').first()
    compras_abertas = IndicadoresCompra.objects.all().values('compras_abertas').first()
    inadimplencia = IndicadoresCompra.objects.all().values('inadimplencia').first()
    referencia = Periodo.objects.filter(situacao='ATUAL').values('sigla').first()
    context = {
        'compras_mes': compras_mes,
        'compras_abertas': compras_abertas,
        'inadimplencia': inadimplencia,
        'referencia': referencia
    }
    return render(request=request, template_name='mercadorias.html', context=context)

def financeiro(request):
    receber_aberto = FinanceiroReceber.objects.all().values('aberto').first()
    receber_inadimplencia = FinanceiroReceber.objects.all().values('inadimplencia').first()
    pagar_aberto = FinanceiroPagar.objects.all().values('aberto').first()
    pagar_inadimplencia = FinanceiroPagar.objects.all().values('inadimplencia').first()
    referencia = Periodo.objects.filter(situacao='ATUAL').values('sigla').first()
    context = {
        'receber_aberto': receber_aberto,
        'receber_inadimplencia': receber_inadimplencia,
        'pagar_aberto': pagar_aberto,
        'pagar_inadimplencia': pagar_inadimplencia,
        'chart_financeiro_operacao': chart_financeiro_operacao(),
        'referencia': referencia
    }
    return render(request=request, template_name='financeiro.html', context=context)

def resultado(request):
    creditos = ResultadoAtual.objects.filter(natureza='CREDITO').aggregate(total=Sum('valor_original'))
    debitos = ResultadoAtual.objects.filter(natureza='DEBITO').aggregate(total=Sum('valor_original'))
    resultado = ResultadoAtual.objects.aggregate(total=Sum('valor'))
    referencia = Periodo.objects.filter(situacao='ATUAL').values('sigla').first()
    context = {
        'creditos': creditos,
        'debitos': debitos,
        'resultado': resultado,
        'chart_resultado_atual': chart_resultado_atual(),
        'chart_resultado_geral': chart_resultado_geral(),
        'chart_resultado_geral_atual': chart_resultado_geral(),
        'referencia': referencia
    }
    return render(request=request, template_name='resultado.html', context=context)

def producao(request):
    referencia = Periodo.objects.filter(situacao='ATUAL').values('sigla').first()
    context = {
        'referencia': referencia
    }
    return render(request=request, template_name='producao.html', context=context)

def consulta(request):
    context = {
    }
    return render(request=request, template_name='consulta.html', context=context)

def disponibilidade(request):
    caixa_debito = DisponibilidadeCaixa.objects.aggregate(total=Sum('debito'))
    caixa_credito = DisponibilidadeCaixa.objects.aggregate(total=Sum('credito'))
    banco_debito = DisponibilidadeBanco.objects.aggregate(total=Sum('debito'))
    banco_credito = DisponibilidadeBanco.objects.aggregate(total=Sum('credito'))
    cartao_debito = DisponibilidadeCartao.objects.aggregate(total=Sum('debito'))
    cartao_credito = DisponibilidadeCartao.objects.aggregate(total=Sum('credito'))
    caixa = DisponibilidadeCaixa.objects.all()
    banco = DisponibilidadeBanco.objects.all()
    cartao = DisponibilidadeCartao.objects.all()
    context = {
        'caixa': caixa,
        'banco': banco,
        'cartao': cartao,
        'caixa_debito': caixa_debito,
        'caixa_credito': caixa_credito,
        'banco_debito': banco_debito,
        'banco_credito': banco_credito,
        'cartao_debito': cartao_debito,
        'cartao_credito': cartao_credito,
    }
    return render(request=request, template_name='disponibilidade.html', context=context)