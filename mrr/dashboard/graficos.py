import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_gauge(total, titulo, arquivo):
    if not total:
        total = 0

    if total < 0:
        cor = "crimson"
        total *= -1
    else:
        cor = "royalblue"

    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = total,
        title = {
            "text":titulo,
            "font":{
                "size":12,
            },
        },
        number = {
            "prefix": "R$"
        },        
        domain = {
            'x': [0, 1], 'y': [0, 1]
        },
        gauge = {
            "bar": {"color":cor}
        }
    ))
    fig.update_layout(
        height=100,
        margin=dict(l=15, r=15, t=45, b=10)
    )
    fig.write_html(os.path.join(BASE_DIR, "dashboard","templates/dashboard/", arquivo + ".html"), config={'displayModeBar': False})
    
def get_line(df, x, y, arquivo, titulo=""):
    fig = px.line(df, x=x, y=y, title=titulo, template="plotly_white")
    

    fig.update_layout(  
        height=230,
        margin=dict(l=15, r=15, t=25, b=0),
        showlegend=False,
    )
    fig.write_html(os.path.join(BASE_DIR, "dashboard","templates/dashboard/", arquivo + ".html"), config={'displayModeBar': False})

def get_bar(df, nomes, count, arquivo, titulo="", colorscale="Teal", orientation="v"):

    flag = 1
    if not len(df):
        df = pd.DataFrame.from_dict({nomes:[0],count:[0]})
        flag = 0

    fig = px.bar(df, x=nomes, y=count, color=count, template="plotly_white", title=titulo, color_continuous_scale=colorscale, orientation=orientation)
    if flag:
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(
        height=230,
        margin=dict(l=0, r=15, t=25, b=0),
        uniformtext_minsize=8,
        uniformtext_mode='hide'
    )

    fig.write_html(os.path.join(BASE_DIR, "dashboard","templates/dashboard/", arquivo + ".html"), config={'displayModeBar': False})

def get_pie(df, valores, nomes, arquivo, titulo=""):
    fig = px.pie(df, values=valores, names=nomes, title=titulo, template="plotly_white")

    fig.update_traces(
        textposition='inside',
        textinfo='percent+label',
    )

    fig.update_layout(
        height=175,
        margin=dict(l=15, r=15, t=45, b=10),
        showlegend=False
    )

    fig.write_html(os.path.join(BASE_DIR, "dashboard","templates/dashboard/", arquivo + ".html"), config={'displayModeBar': False})