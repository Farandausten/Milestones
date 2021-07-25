from dash_html_components.H1 import H1
#import plotly.express as px
import pandas as pd
#import dash
#import dash_core_components as dcc
import dash_html_components as html
#from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
#import statsmodels.api as sm
#import statsmodels.formula.api as smf
#from statsmodels.stats.anova import anova_lm
#import scipy.stats as stats
import dash_table
from statsmodels.stats.multicomp import pairwise_tukeyhsd
 
from app import app #change this line
 
# Data Preprocessing
dg = pd.read_csv('supermarket_sales - Sheet1.csv')
dg = dg.rename(
        columns = {
            "Product line" : "Product_line",
            "Customer type" : "Customer_type"
        })
#1.         
tukey = pairwise_tukeyhsd(endog =dg['Total'],
                         groups = dg['City'],
                         alpha =0.05)  
dh = pd.DataFrame(tukey.summary().data[1:], columns = tukey.summary().data[0])                         

#2. 
tukey2 = pairwise_tukeyhsd(endog =dg['Total'],
                         groups = dg['Branch'],
                         alpha =0.05)  
di = pd.DataFrame(tukey2.summary().data[1:], columns = tukey2.summary().data[0])

#3. 
tukey3 = pairwise_tukeyhsd(endog =dg['Total'],
                         groups = dg['Customer_type'],
                         alpha =0.05)  
dj = pd.DataFrame(tukey3.summary().data[1:], columns = tukey3.summary().data[0])

#4.
tukey4 = pairwise_tukeyhsd(endog =dg['Total'],
                         groups = dg['Gender'],
                         alpha =0.05)  
dk = pd.DataFrame(tukey4.summary().data[1:], columns = tukey4.summary().data[0])

#5. 
tukey5 = pairwise_tukeyhsd(endog =dg['Total'],
                         groups = dg['Product_line'],
                         alpha =0.05)  
dl = pd.DataFrame(tukey5.summary().data[1:], columns = tukey5.summary().data[0])

#6.
tukey6 = pairwise_tukeyhsd(endog =dg['Total'],
                         groups = dg['Payment'],
                         alpha =0.05)  
dn = pd.DataFrame(tukey6.summary().data[1:], columns = tukey6.summary().data[0])

# 7.
# 8.
# 9.
# 10.  


layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1(children="ANOVA TESTING"),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='Analisis one way Anova atau uji anova satu faktor pada dasarnya bertujuan untuk membandingkan nilai rata-rata yang terdapat pada variabel terikat di semua kelompok yang dibandingkan. Nilai masing-masing kelompok dilihat berdasarkan pada variabel bebas yang berskala kategori. Analisis anova peruluasan dari teknik independent sample t-test. Anova dapat digunakan untuk kelompok yang berjumlah lebih dari 2 serta mempunyai nilai rata-rata yang sama ataupun berbeda'),
                className="mb-4"
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.H6(children='H0 : Memiliki varian yang sedikit berbeda, bisa dilakukan lebih dari 2 kelompok'),
                    html.H6(children='H1 : Memiliki varian yang sangat berbeda, bisa dilakukan lebih dari 2 kelompok')
                ],    
                    className="mb-4"
            ))
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Hubungan antara values dari kolom City dengan Nilai Total'), 
                    html.P(children='Pada tabel dibawah ini:'),
                ])
            )
        ]), 

        dbc.Row([
            dbc.Col(
                dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in dh.columns],
                data = dh.to_dict('records'),
                
                )
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Bisa terlihat dari kolom p-adj / p value, jika > 0.05 dan statusnya reject H1'), 
                    html.P(children='- False = Menerima h0'),
                    html.P(children='- True = Menolak h0'),
                    html.P(children='Yang dapat disimpulkan bahwa:'),
                    html.P(children='1. Mandalay dan Napitau dengan Nilai Total, varian yang sama'),
                    html.P(children='2. Mandalay dan Yangon dengan Nilai Total, varian yang sama'),
                    html.P(children='3. Yangon dan Napitau dengan Nilai Total, varian yang sama'),

                ],
                className="mb-4"
                )
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Hubungan antara values dari kolom Branch dengan Nilai Total'), 
                    html.P(children='Pada tabel dibawah ini:'),
                ],
                className="mt-4")
            )
        ]),  


        dbc.Row([
            dbc.Col(
                dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in di.columns],
                data =di.to_dict('records'),
                
                )
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Bisa terlihat dari kolom p-adj / p value, jika > 0.05 dan statusnya reject H1'), 
                    html.P(children='- False = Menerima h0'),
                    html.P(children='- True = Menolak h0'),
                    html.P(children='Yang dapat disimpulkan bahwa:'),
                    html.P(children='1. A dan B dengan Nilai Total, varian yang sama'),
                    html.P(children='2. A dan C dan Yangon dengan Nilai Total, varian yang sama'),
                    html.P(children='3. B dan C dengan Nilai Total, varian yang sama'),
                ],
                className="mb-4"
                )
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Hubungan antara values dari kolom Customer_type dengan Nilai Total'), 
                    html.P(children='Pada tabel dibawah ini:'),
                ],
                className="mt-4")
            )
        ]),  

        dbc.Row([
            dbc.Col(
                dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in dj.columns],
                data =dj.to_dict('records'),
                
                )
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Bisa terlihat dari kolom p-adj / p value, jika > 0.05 dan statusnya reject H1'), 
                    html.P(children='- False = Menerima h0'),
                    html.P(children='- True = Menolak h0'),
                    html.P(children='Yang dapat disimpulkan bahwa:'),
                    html.P(children='1. Member dan Normal dengan Nilai Total, varian yang sama'),
                ],
                className="mb-4"
                )
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Hubungan antara values dari kolom Gender dengan Nilai Total'), 
                    html.P(children='Pada tabel dibawah ini:'),
                ],
                className="mt-4")
            )
        ]),  

        dbc.Row([
            dbc.Col(
                dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in dk.columns],
                data =dk.to_dict('records'),
                
                )
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Bisa terlihat dari kolom p-adj / p value, jika > 0.05 dan statusnya reject H1'), 
                    html.P(children='- False = Menerima h0'),
                    html.P(children='- True = Menolak h0'),
                    html.P(children='Yang dapat disimpulkan bahwa:'),
                    html.P(children='1. Male dan Female  dengan Nilai Total, varian yang sama'),
                ],
                className="mb-4"
                )
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Hubungan antara values dari kolom Product Line dengan Nilai Total'), 
                    html.P(children='Pada tabel dibawah ini:'),
                ],
                className="mt-4")
            )
        ]),  

        dbc.Row([
            dbc.Col(
                dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in dl.columns],
                data =dl.to_dict('records'),
                
                )
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Bisa terlihat dari kolom p-adj / p value, jika > 0.05 dan statusnya reject H1'), 
                    html.P(children='- False = Menerima h0'),
                    html.P(children='- True = Menolak h0'),
                    html.P(children='Yang dapat disimpulkan bahwa:'),
                    html.P(children='1. Electronic accessories dan Food and beverages dengan Nilai Total, varian yang sama'),
                    html.P(children='2. Electronic accessories dan Health and beauty dengan Nilai Total, varian yang sama'),
                    html.P(children='3. Electronic accessories dan Sports and travel dengan Nilai Total, varian yang sama'),
                    html.P(children='4. Fashion accessories dan Food and beverages dengan Nilai Total, varian yang sama'),
                    html.P(children='5. Sports and travel dan Food and beverages dengan Nilai Total, varian yang sama'),
                    html.P(children='Dan Lain Sebagainya bisa dilihat dari tabel'),

                ],
                className="mb-4"
                )
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Hubungan antara values dari kolom Payment dengan Nilai Total'), 
                    html.P(children='Pada tabel dibawah ini:'),
                ],
                className="mt-4")
            )
        ]),  

        dbc.Row([
            dbc.Col(
                dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in dn.columns],
                data =dn.to_dict('records'),
                
                )
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Bisa terlihat dari kolom p-adj / p value, jika > 0.05 dan statusnya reject H1'), 
                    html.P(children='- False = Menerima h0'),
                    html.P(children='- True = Menolak h0'),
                    html.P(children='Yang dapat disimpulkan bahwa:'),
                    html.P(children='1. Cash dan Credit card  dengan Nilai Total, varian yang sama'),
                    html.P(children='2. Cash dan Ewallet dengan Nilai Total, varian yang sama'),
                    html.P(children='3. Credit card dan Ewallet dengan Nilai Total, varian yang sama'),
                ],
                className="mb-4"
                )
            )
        ]),
        
        
        ])
    ])
 