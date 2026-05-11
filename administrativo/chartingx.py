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



