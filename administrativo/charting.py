import pandas as pd
import plotly.express as px


def chart_example():
    df = pd.DataFrame(
        {
            'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Bananas'],
            'Amount': [4, 1, 2, 3, 4, 5],
            'City': ['SP', 'SP', 'SP', 'RJ', 'RJ', 'RJ']
        }
    )
    return px.bar(
        df,
        x='Fruit',
        y='Amount',
        color='City',
        title='Fruit Amounts',
        color_discrete_sequence=px.colors.qualitative.T10,
        width=500,
        height=500,
        template="simple_white",
    ).to_html()

