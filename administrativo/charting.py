import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
from sklearn.decomposition import PCA

from .models import (
    Acessorio,
    VendasTipoCliente,
    VendasTipoCategoria,
    VendasCategoriaTipo,
    ClientesRFM,
    VendasCurvaABC,
    CategoriaProduto,
    CustosCurvaABC,
    ProducaoCategoria,
    ProducaoDiaria,
    ProducaoDiariaCategoria,
    MercadoriaCurvaABC,
    ComprasSegmento,
    ConsumoMercadoria,
    ResultadoAtual,
    ResultadoGeral,
    ResultadoGeralAtual,
    FinanceiroLancamento,
    FinanceiroOperacao,
    InicioEconomico,
    InicioFinanceiro
)

def chart_example():
    df_acessorio = pd.DataFrame(list(Acessorio.objects.all().values()))
    return go.Figure(data=[go.Table(
        header=dict(values=list(df_acessorio.columns),
                    fill_color='lightskyblue',
                    align='left'),
        cells=dict(values=[df_acessorio[col] for col in df_acessorio.columns],
                   fill_color='lightcyan',
                   align='left'))
    ]).to_html()

def chart_tipo_cliente():
    df = pd.DataFrame(
        list(VendasTipoCliente.objects.all().values())
    )
    return px.sunburst(
        data_frame=df,
        path=['tipo', 'cliente'],
        values='valor',
        color_discrete_sequence=px.colors.qualitative.T10
    ).update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)"
    ).to_html()

def chart_tipo_categoria():
    df = pd.DataFrame(
        list(VendasTipoCategoria.objects.all().values())
    )
    return px.sunburst(
        data_frame=df,
        path=['tipo', 'categoria', 'produto'],
        values='valor',
        color_discrete_sequence=px.colors.qualitative.T10
    ).update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)"
    ).to_html()

def chart_categoria_tipo():
    df = pd.DataFrame(
        list(VendasCategoriaTipo.objects.all().values())
    )
    return px.sunburst(
        data_frame=df,
        path=['categoria', 'tipo', 'produto'],
        values='valor',
        color_discrete_sequence=px.colors.qualitative.T10
    ).update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)"
    ).to_html()

def chart_rfpm():
    df = pd.DataFrame(list(ClientesRFM.objects.all().values()))
    df['rfpm'] = df['rfpm'].astype(int)
    return px.bar(
        data_frame=df,
        x='cliente',
        y='rfpm',
        text_auto='rfpm',
        hover_data=['recente', 'frequencia', 'pago', 'montante']
    ).update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        xaxis={"categoryorder": "total descending"},
    ).to_html()

def chart_pca():
    df = pd.DataFrame(list(ClientesRFM.objects.all().values()))
    variaveis = ['recente', 'frequencia', 'pago', 'montante']
    pca = PCA(n_components=2).fit(df[variaveis]).transform(df[variaveis])
    df['escala_X'] = pca[:, 0]
    df['escala_Y'] = pca[:, 1]
    return px.scatter(
        data_frame=df,
        x='escala_X',
        y='escala_Y',
        text='cliente',
        hover_data = ['recente', 'frequencia', 'pago', 'montante']
    ).update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        height=800
    ).update_traces(textposition="bottom right").to_html()


def chart_curva_abc():
    df = pd.DataFrame(list(VendasCurvaABC.objects.all().values()))
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Bar(x=df['produto'], y=df['total'], name='Valor',
        marker = dict(
            color=df['curva'].map({'A': 'green', 'B': 'yellow', 'C': 'red'}),
        ),
        text = df['curva'],
        textposition = 'auto'
        ),
        secondary_y=False
    )
    fig.add_trace(
        go.Scatter(x=df['produto'], y=df['cumulativo'], name='Cumulativo %', mode='lines+markers', line=dict(color='blue')),
        secondary_y=True
    )
    fig.update_layout(title='Curva ABC (Pareto)', xaxis_title='Produto', yaxis_title='Valor')
    fig.update_yaxes(title_text='Cumulativo %', secondary_y=True, range=[0, 105])
    fig.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        height=800
    )
    return fig.to_html()

def chart_categoria_produto():
    df = pd.DataFrame(
        list(CategoriaProduto.objects.all().values())
    )
    return px.sunburst(
        data_frame=df,
        path=['categoria', 'produto'],
        values='total',
        color_discrete_sequence=px.colors.qualitative.T10
    ).update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)"
    ).to_html()

def chart_custos_abc():
    df = pd.DataFrame(list(CustosCurvaABC.objects.all().values()))
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Bar(x=df['produto'], y=df['total'], name='Valor',
        marker = dict(
            color=df['curva'].map({'A': 'green', 'B': 'yellow', 'C': 'red'}),
        ),
        text = df['curva'],
        textposition = 'auto'
        ),
        secondary_y=False
    )
    fig.add_trace(
        go.Scatter(x=df['produto'], y=df['cumulativo'], name='Cumulativo %', mode='lines+markers', line=dict(color='blue')),
        secondary_y=True
    )
    fig.update_layout(title='Curva ABC (Pareto)', xaxis_title='Produto', yaxis_title='Valor')
    fig.update_yaxes(title_text='Cumulativo %', secondary_y=True, range=[0, 105])
    fig.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        height=800
    )
    return fig.to_html()


def chart_producao_categoria():
    df = pd.DataFrame(
        list(ProducaoCategoria.objects.all().values())
    )
    return px.sunburst(
        data_frame=df,
        path=['categoria', 'produto'],
        values='quantidade',
        color_discrete_sequence=px.colors.qualitative.T10
    ).update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)"
    ).to_html()

def chart_producao_diaria_categoria():
    df = pd.DataFrame(
        list(ProducaoDiariaCategoria.objects.all().values())
    )
    return px.sunburst(
        data_frame=df,
        path=['dia', 'categoria', 'produto'],
        values='quantidade',
        color_discrete_sequence=px.colors.qualitative.T10
    ).update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)"
    ).to_html()

def chart_producao_diaria():
    df = pd.DataFrame(list(ProducaoDiaria.objects.all().values()))
    return px.bar(
        data_frame=df,
        x='dia',
        y='total',
        text_auto='total',
    ).update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        xaxis={"categoryorder": "category ascending"},
    ).to_html()

def chart_mercadoria_abc():
    df = pd.DataFrame(list(MercadoriaCurvaABC.objects.all().values()))
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Bar(x=df['ingrediente'], y=df['total'], name='Valor',
        marker = dict(
            color=df['curva'].map({'A': 'green', 'B': 'yellow', 'C': 'red'}),
        ),
        text = df['curva'],
        textposition = 'auto'
        ),
        secondary_y=False
    )
    fig.add_trace(
        go.Scatter(x=df['ingrediente'], y=df['cumulativo'], name='Cumulativo %', mode='lines+markers', line=dict(color='blue')),
        secondary_y=True
    )
    fig.update_layout(title='Curva ABC (Pareto)', xaxis_title='ingrediente', yaxis_title='Valor')
    fig.update_yaxes(title_text='Cumulativo %', secondary_y=True, range=[0, 105])
    fig.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        height=800
    )
    return fig.to_html()

def chart_compras_segmento():
    df = pd.DataFrame(
        list(ComprasSegmento.objects.all().values())
    )
    return px.sunburst(
        data_frame=df,
        path=['segmento', 'ingrediente'],
        values='total',
        color_discrete_sequence=px.colors.qualitative.T10
    ).update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)"
    ).to_html()

def chart_consumo_mercadoria():
    df = pd.DataFrame(
        list(ConsumoMercadoria.objects.all().values())
    )
    return px.sunburst(
        data_frame=df,
        path=['segmento', 'ingrediente'],
        values='total',
        color_discrete_sequence=px.colors.qualitative.T10
    ).update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)"
    ).to_html()

def chart_resultado_atual():
    df = pd.DataFrame(list(ResultadoAtual.objects.all().values()))
    fig = go.Figure(go.Waterfall(
        x=list(df['conta']),
        y=list(df['valor']),
        textposition="outside",
        text=list(df['valor']),
    ))
    fig.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
    )
    return fig.to_html()

def chart_resultado_geral():
    df = pd.DataFrame(
        list(ResultadoGeral.objects.all().values())
    )
    return px.treemap(
        data_frame=df,
        path=['nivel1', 'nivel2', 'nivel3'],
        values='saldo',
        color_discrete_sequence=px.colors.qualitative.T10
    ).update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)"
    ).to_html()

def chart_resultado_geral_atual():
    df = pd.DataFrame(
        list(ResultadoGeralAtual.objects.all().values())
    )
    return px.treemap(
        data_frame=df,
        path=['nivel1', 'nivel2', 'nivel3', 'natureza'],
        values='valor',
        color_discrete_sequence=px.colors.qualitative.T10
    ).update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)"
    ).to_html()

def chart_financeiro_lancamento_data():
    df = pd.DataFrame(
        list(FinanceiroLancamento.objects.all().values())
    )
    return px.treemap(
        data_frame=df,
        path=['data', 'operacao', 'pessoa'],
        values='valor',
        color_discrete_sequence=px.colors.qualitative.T10
    ).update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)"
    ).to_html()

def chart_financeiro_lancamento_operacao():
    df = pd.DataFrame(
        list(FinanceiroLancamento.objects.all().values())
    )
    return px.treemap(
        data_frame=df,
        path=['operacao', 'data', 'pessoa'],
        values='valor_original',
        color_discrete_sequence=px.colors.qualitative.T10
    ).update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)"
    ).to_html()

def chart_financeiro_operacao():
    df = pd.DataFrame(list(FinanceiroOperacao.objects.all().values()))
    fig = go.Figure(go.Waterfall(
        x=[list(df['dia']), list(df['operacao'])],
        y=list(df['valor']),
        textposition="outside",
        text=list(df['valor']),
    ))
    fig.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        height=800
    )
    return fig.to_html()

def chart_inicio_economico():
    df = pd.DataFrame(list(InicioEconomico.objects.all().values()))
    fig = go.Figure(go.Waterfall(
        x=[list(df['dia']), list(df['tipo'])],
        y=list(df['valor']),
        textposition="outside",
        text=list(df['valor']),
    ))
    fig.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
    )
    return fig.to_html()

def chart_inicio_financeiro():
    df = pd.DataFrame(list(InicioFinanceiro.objects.all().values()))
    fig = go.Figure(go.Waterfall(
        x=[list(df['dia']), list(df['tipo'])],
        y=list(df['valor']),
        textposition="outside",
        text=list(df['valor']),
    ))
    fig.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
    )
    return fig.to_html()