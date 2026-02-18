import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from .models import Acessorio

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

