import plotly.graph_objects as go
import plotly.express as px

def plot_line_chart(df, title, x_label, y_labels, ideal):
    x = len(df)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df[x_label], y=ideal, name="Ideal", line_shape='linear'))
    for y_label in y_labels:
        fig.add_trace(go.Scatter(x=df[x_label], y=df[y_label], name=y_label, line_shape='spline'))

    annotations = []
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05, xanchor='left', yanchor='bottom', text=f'{title} for last {x} weeks', showarrow=False))
    fig.update_layout(annotations=annotations)

    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(
                visible=True
            ),
            type="category"
        )
    )

    return fig


def plot_line_chart_with_bar(df, title, x_label, y_labels, bar_label, ideal):
    x = len(df)

    fig = go.Figure(
        data=[go.Bar(y=[0] + list(df[bar_label]), name=bar_label)],
    )
    fig.add_trace(go.Scatter(x=df[x_label], y=ideal, name="Ideal", line_shape='linear'))
    for y_label in y_labels:
        fig.add_trace(go.Scatter(x=df[x_label], y=df[y_label], name=y_label, line_shape='spline'))

    annotations = []
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05, xanchor='left', yanchor='bottom', text=f'{title} for last {x} weeks', showarrow=False))
    fig.update_layout(annotations=annotations)

    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(
                visible=True
            ),
            type="category"
        )
    )

    return fig


def plot_pie_chart(df, title, key, value):
    fig = px.pie(df, values=value, names=key, title=title)
    return fig


def plot_table_chart(df):
    rowEvenColor = 'lightgrey'
    rowOddColor = 'white'

    header = list(df.columns)
    isOdd = len(df.index) % 2 == 0
    fig = go.Figure(data=[go.Table(
            header=dict(
                values=header,
                line_color='darkslategray',
                fill_color='grey',
                align=['left','center'],
            ),
            cells=dict(
                values=[df[i] for i in header],
                line_color='darkslategray',
                fill_color=[
                        [rowOddColor, rowEvenColor, rowOddColor, rowEvenColor] * (len(df.index) // 2) + [rowOddColor]
                        if isOdd
                        else [rowOddColor, rowEvenColor, rowOddColor, rowEvenColor] * (len(df.index) // 2)
                    ],
                align='left'
            )
        )
    ])

    return fig
