# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import os

import dash
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

from dash import dcc
from dash import html
from helpers import (
    get_merge_rate_dataframe,
    get_open_to_merge_dataframe,
    get_open_to_merge_week_dataframe,
    get_pr_size_week_dataframe,
    get_pr_size_metrics_dataframe,
    get_open_to_merge_for_last_week_dataframe,
    get_time_to_review_dataframe,
    get_time_to_open_dataframe,
    get_time_to_merge_dataframe,
)
from plots import plot_line_chart, plot_line_chart_with_bar, plot_pie_chart
from constants import (
    IDEAL_MERGE_RATE, IDEAL_OPEN_TO_MERGE, IDEAL_PR_SIZE, IDEAL_TIME_TO_REVIEW,
    IDEAL_TIME_TO_OPEN, IDEAL_TIME_TO_MERGE
)

app = dash.Dash(__name__)

server = app.server

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

merge_rate_df = get_merge_rate_dataframe()
ideal_merge_rate = np.repeat(IDEAL_MERGE_RATE, len(merge_rate_df))
fig_merge_rate = plot_line_chart(merge_rate_df, "Merge Rate", "Week", ["Merge Rate"], ideal_merge_rate)

open_to_merge_df = get_open_to_merge_dataframe()
ideal_open_to_merge = np.repeat(IDEAL_OPEN_TO_MERGE, len(open_to_merge_df))
fig_open_to_merge = plot_line_chart(open_to_merge_df, "Open to Merge Time", "Week", ["Mean", "Median", "Percentile 95"], ideal_open_to_merge)

pr_size_metrics_df = get_pr_size_metrics_dataframe()
ideal_pr_size = np.repeat(IDEAL_PR_SIZE, len(pr_size_metrics_df))
fig_pr_size = plot_line_chart_with_bar(pr_size_metrics_df, "PR Size", "Week", ["Mean", "Median", "Percentile 95"], "Max Additions", ideal_pr_size)

open_to_merge_by_author = get_open_to_merge_for_last_week_dataframe()
fig_open_to_merge_by_author = plot_pie_chart(open_to_merge_by_author, "Last Week Open to Merge Time by Author", "Author", "Duration in hours")

time_to_review_df = get_time_to_review_dataframe()
ideal_time_to_review = np.repeat(IDEAL_TIME_TO_REVIEW, len(time_to_review_df))
fig_time_to_review = plot_line_chart(time_to_review_df, "Time to Review", "Week", ["Mean", "Median", "Percentile 95"], ideal_time_to_review)

time_to_open_df = get_time_to_open_dataframe()
ideal_time_to_open = np.repeat(IDEAL_TIME_TO_OPEN, len(time_to_open_df))
fig_time_to_open = plot_line_chart(time_to_open_df, "Time to Open", "Week", ["Mean", "Median", "Percentile 95"], ideal_time_to_open)

time_to_merge_df = get_time_to_merge_dataframe()
ideal_time_to_merge = np.repeat(IDEAL_TIME_TO_MERGE, len(time_to_merge_df))
fig_time_to_merge = plot_line_chart(time_to_merge_df, "Time to Merge", "Week", ["Mean", "Median", "Percentile 95"], ideal_time_to_merge)

app.layout = html.Div(children=[
    html.H1(children='Dashboard'),

    html.Div(children='''
        Metrics for https://github.com/rsarai/scrapping-metrics
    '''),
    html.Div([
        dcc.Graph(
            id='Merge Rate',
            figure=fig_merge_rate
        ),
        dcc.Graph(
            id='Merge Time',
            figure=fig_open_to_merge
        ),
    ], style={'display': 'flex', 'width': '100%'}),
    html.Div([
        dcc.Graph(
            id='Merge Time By Author',
            figure=fig_open_to_merge_by_author
        ),
    ], style={'height': '100%'}),
    html.Div([
        dcc.Graph(
            id='PR Size',
            figure=fig_pr_size
        ),
        dcc.Graph(
            id='Time to review',
            figure=fig_time_to_review
        ),
    ], style={'display': 'flex', 'width': '100%'}),
    html.Div([
        dcc.Graph(
            id='Time to Open',
            figure=fig_time_to_open
        ),
        dcc.Graph(
            id='Time to Merge',
            figure=fig_time_to_merge
        ),
    ], style={'display': 'flex', 'width': '100%'}),
])

if __name__ == '__main__':
    app.run_server(debug=True)
