import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
#from dash_html_components.Div import Div
import plotly.express as px
import pandas as pd
import numpy as np

from app import app
 
df = pd.read_csv('supermarket_sales - Sheet1.csv')
df = df.rename(
        columns = {
            "Product line" : "Product_line"
        })

#deklarasi layout
# DIV > H1 > HELLO DASH         
layout = html.Div(children=[
    html.Div(
        children=[
            html.H1(children= "Grafik Laju Pada Supermarket Sales Jika Total Naik", className="header-emoji"),
            html.H1(
                children ="",
                className="header-description",
            ),
        ],
        className="header",
    ),
    html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(children="Product_line", className = "menu-title"),
                    dcc.Dropdown(
                        id="region-filter",
                        options =[
                        {"label" : Product_line, "value" : Product_line}
                        for Product_line in np.sort(df.Product_line.unique())
                        ],
                        value = 'branch',
                        clearable=False,
                        className='dropdown',
                    ),
                ]
        ),
            html.Div(
                children=[
                    html.Div(children="Type", className = "menu-title"),
                    dcc.Dropdown(
                        id="type-filter",
                        options =[
                            {"label" : Gender, "value" : Gender}
                            for Gender in df.Gender.unique()
                        ],
                        value ='male',
                        clearable=False,
                        searchable=False,
                        className='dropdown'
                    ),
                ]
            ),

        ],
        className="menu",
    ),
    html.Div(
        children=[
            html.Div(
                children = dcc.Graph(
                    id = "price-chart"
                    ),

                className = "card",
            ),
            html.Div(
                children = dcc.Graph(
                    id = "total-chart"
                    ),

                className = "card",
            ),
            html.Div(
                children = dcc.Graph(
                    id = "tax-chart"
                    ),

                className = "card",
            ),
            html.Div(
                children = dcc.Graph(
                    id = "grass-chart"
                    
                    ),

                className = "card",
            ),     
        ],
        className= "wrapper"
    )
]
)

           

@app.callback(
    [
     Output("price-chart", "figure"),
     Output("total-chart", "figure"), 
     Output("tax-chart", "figure"), 
     Output("grass-chart", "figure")  
    ],
    [
     Input("region-filter", "value"),
     Input("type-filter", "value")
    ],
)    
def update_charts(Product_line, Gender):
    filtered_df = df[(df.Product_line.isin([Product_line])) &
                     (df.Gender.isin([Gender]))]

    fig = px.scatter(filtered_df, x = "Total", y = "Unit price",
           size="Quantity", color="Payment", hover_name="City",
           log_x=True, size_max=55, title='Laju Unit Price')

    fig2 = px.scatter(filtered_df, x = "Total", y = "Tax 5%",
           size="Quantity", color="Payment", hover_name="City",
           log_x=True, size_max=55, title='Laju Tax')


    fig3 = px.scatter(filtered_df, x = "Total", y = "gross income",
                     size="Quantity", color="Payment", hover_name="City",
                     log_x=True, size_max=55, title='Laju Gross Income')


    fig4 = px.scatter(filtered_df, x = "Total", y = "Rating",
                     size="Quantity", color="Payment", hover_name="City",
                     log_x=True, size_max=55, title='Rating')
    
 
    return fig, fig2, fig3, fig4
