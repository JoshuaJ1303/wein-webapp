import pandas as pd
import plotly.express as px
import plotly
import json

def create_barchart(df: pd.DataFrame, ID: str)-> json:
    """
    creates a json object to display a plotly chart.

    args: 
    df (pd.Dataframe)
    ID (str): ID column the chart is based on.

    returns: 
    Json for Plotly
    """

    # Bar chart data: Count of a specific column (e.g., 'Column1')

    bar_counts = df[ID].value_counts().reset_index()
    bar_counts.columns = [ID, 'Count']
    # Create figures for Plotly
    bar_fig = px.bar(bar_counts, x=ID, y='Count', title=f'Count of {ID}')
    # Convert Plotly figures to JSON for rendering in HTML
    bar_fig_json = bar_fig.to_json()

    return bar_fig_json



def create_piechart(df: pd.DataFrame, ID: str)-> json:
    """
    creates a json object to display a plotly chart.

    args: 
    df (pd.Dataframe)
    ID (str): ID column the chart is based on.

    returns: 
    Json for Plotly
    """
    # Pie chart data: Count of another specific column (e.g., 'Column2')
    pie_counts = df[ID].value_counts().reset_index()
    pie_counts.columns = [ID, 'Count']

    pie_fig = px.pie(pie_counts, names=ID, values='Count', title=f'Counts of {ID}')
    pie_fig_json = pie_fig.to_json()

    return pie_fig_json