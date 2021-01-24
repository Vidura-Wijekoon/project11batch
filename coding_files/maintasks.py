# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 10:18:22 2021

@author: user pc vidura97
"""

# https://pastebin.com/D86LbREX

import pickle
import pandas as pd
import webbrowser
# !pip install dash
import dash
import dash_html_components as html
import dash_core_components as dcc
import numpy as np
from dash.dependencies import State
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output 
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import plotly.graph_objects as go
from pandas_datareader import data as web

import plotly           #(version 4.5.4) #pip install plotly==4.5.4
import plotly.express as px
import plotly.io as pio
# Declaring Global variables
# A variable declared outside a function is a global variable by default.
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])




app = dash.Dash(external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'])

colors = {'background': '#ffffff',
          'bg_home': '#666666',
          'text': '#ffa500',
          'background_plot': '#cccccc',
          'text_plot': '#000000'}



app.config['suppress_callback_exceptions']=True

df = pd.read_csv('D:/Internships/Forsk_batch11_ViduraWijekoon/Csv_datasets/balanced_reviews.csv')
(df.columns.tolist())

df['overall'].value_counts()

df.isnull().any(axis = 0)

df.isnull().any(axis = 1)

df[df.isnull().any(axis = 1)].tail()


#handling the missing data
df.dropna(inplace = True)


df['Positivity'] = np.where(df['overall'] > 3, 1, 0)

labels = ['Positive Reviews', 'Negative Reviews']
values = [len(df[df.Positivity == 1]), len(df[df.Positivity == 0])]

df1 = pd.read_csv('D:/Internships/Forsk_batch11_ViduraWijekoon/Csv_datasets/Review_data.csv')
(df1.columns.tolist())

df1['Ratings'].value_counts()

df1.isnull().any(axis = 0)

df1.isnull().any(axis = 1)

df1[df1.isnull().any(axis = 1)].tail()


#handling the missing data
df1.dropna(inplace = True)


df1['Positivity'] = np.where(df1['Ratings'] > 3, 1, 0)

dff = df1  
box_style = dict(border='1px solid', margin='15px', padding='10px')
project_name = None

def load_model():
    global df
    df = pd.read_csv('D:/Internships/Forsk_batch11_ViduraWijekoon/Csv_datasets/balanced_reviews.csv')
  
    global pickle_model
    file = open("pickle_model.pkl", 'rb') 
    pickle_model = pickle.load(file)

    global vocab
    file = open("feature.pkl", 'rb') 
    vocab = pickle.load(file)
    
    print(df.sample(5))

def open_browser():
    # Open the default web browser
    webbrowser.open_new('http://127.0.0.1:8050/')

def check_review(reviewText):

    #reviewText has to be vectorised, that vectorizer is not saved yet
    #load the vectorize and call transform and then pass that to model preidctor
    #load it later

    transformer = TfidfTransformer()
    loaded_vec = CountVectorizer(decode_error="replace",vocabulary=vocab)
    reviewText = transformer.fit_transform(loaded_vec.fit_transform([reviewText]))


    # Add code to test the sentiment of using both the model
    # [0] == negative   [1] == positive
    return pickle_model.predict(reviewText)

    

image   = 'url(https://c.wallhere.com/photos/a1/fc/1920x1080_px_Albert_Einstein_Formula_mathematics_physics_science_Special_Relativity-549404.jpg!d)'



def create_app_ui():
    # Create the UI of the Webpage here
    main_layout = html.Div(
             [
        
            
            html.H1('Welcome!', style={'color': 'black','text-align': 'center' ,'background-image': 'url(https://s3.amazonaws.com/blog4.0/blog/wp-content/uploads/2018/04/customer-sentiment-analysis-tools.png)'})
                ,
        
        
        html.H1(children='Sentiments Analysis with Insights', id='Main_title',style={'color': 'red','text-align': 'center' }),
        dbc.Container([
                        dcc.Dropdown(
                    id='dropdown',
                    placeholder = 'Select a Review',
                    options=[{'label': i, 'value': i} for i in dff.Reviews.sample(81)],
                        
                        # {'label': 'New York City', 'value': 'NYC'},
                        # {'label': 'Montreal', 'value': 'MTL'},
                        # {'label': 'San Francisco', 'value': 'SF'}
                    value = dff.Reviews[0],
                    style = {'margin-bottom': '30px'}
                    
                )
                       ],
                        style = {'padding-left': '50px', 'padding-right': '50px'}
                        ),
        dbc.Container(
                        dcc.Loading(
                        dcc.Graph(
                            figure = {'data' : [go.Pie(labels=labels, values=values)],
                                      'layout': go.Layout(height = 600, width = 1000, autosize = False),
                                      'paper_bgcolor':'lightblue',
                                      'plot_bgcolr':'lightgrey',
                                      }
                            )
                        ),
                        className = 'd-flex justify-content-center'
                    ),
        
        dcc.Textarea(
            id='textarea_review',
            placeholder='Enter the review here...',
            value='Enter review',
            style={'width': '100%', 'height': 100}
            ),
       
    #butten
       html.Div(
            html.Button(children='Show Review',id = 'show_review', n_clicks=0,style={
        'textAlign': 'center', 'color': colors['text']})),
    
           
     

    #text for review
    dbc.Row(
            [
            html.H3(children=None,id='result')
            ], justify="center", align="center"
            ),
    dbc.Row(
            [
            html.H3(children=None,id='result1'),
            ], justify="center", align="center"
            ),


  
    
    
    
        ])
        
        
    return main_layout

@app.callback(
    Output('result', 'children'),
    [
    Input('show_review', 'n_clicks')
    ],
    state=[State('textarea_review', 'value')]
    )




def update_app_ui(n_clicks,textarea_value):
    
    print("Data Type  = ", str(type(textarea_value)))
    print("Value      = ", str(textarea_value))

    
    result_list = check_review(textarea_value)
    
    if (result_list[0] == 0 and n_clicks > 0):
        result = 'user_input review is Negative'
    elif (result_list[0] == 1 and n_clicks > 0):
        result = 'user_input review is Positive'
    else:
        result = 'user_input review is Unknown'
    
    return result


@app.callback(
    Output('result1', 'children'),
    [
    Input('show_review', 'n_clicks')
    ],
    
    state=[ State('dropdown', 'value') ]
    )




def update_dropdown(n_clicks, value):
    result_list = check_review(value)
    
    if (result_list[0] == 0 and n_clicks > 0):
        result = 'dropdown result is Negative'
    elif (result_list[0] == 1 and n_clicks > 0):
        result = 'dropdown result is Positive'
    else:
        result = 'dropdown result is Unknown'
    
    
    return result
df = pd.read_csv('D:/Internships/Forsk_batch11_ViduraWijekoon/Csv_datasets/balanced_reviews.csv')
(df.columns.tolist())

df['overall'].value_counts()

df.isnull().any(axis = 0)

df.isnull().any(axis = 1)

df[df.isnull().any(axis = 1)].tail()


#handling the missing data
df.dropna(inplace = True)


df['Positivity'] = np.where(df['overall'] > 3, 1, 0)

dff = df

dff1 = dff.groupby('reviewText', as_index=False)[['Positivity']].sum()



df = pd.read_csv('D:/Internships/Forsk_batch11_ViduraWijekoon/Csv_datasets/Review_data.csv')
(df.columns.tolist())

df['Ratings'].value_counts()

df.isnull().any(axis = 0)

df.isnull().any(axis = 1)

df[df.isnull().any(axis = 1)].tail()


#handling the missing data
df.dropna(inplace = True)


df['Positivity'] = np.where(df['Ratings'] > 3, 1, 0)

dff = df  
# Main Function to control the Flow of your Project
def main():
    load_model()    
    open_browser()


    global project_name
    project_name = "Sentiments Analysis with Insights" 
      
    global app
    app.layout = create_app_ui()
    app.title = project_name
    # go to https://www.favicon.cc/ and download the ico file and store in assets directory 
    app.run_server() # debug=True
  
    print("This would be executed only after the script is closed")
    app = None
    project_name = None

if __name__ == '__main__':
    main()
