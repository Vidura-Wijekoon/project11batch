# https://pastebin.com/NFvU2SqP

#importing the libraries
import pickle
import pandas as pd
import webbrowser
# !pip install dash
import dash
import dash_html_components as html
from dash.dependencies import Input, Output 


# Declaring Global variables
# A variable declared outside a function is a global variable by default.
app = dash.Dash()
project_name = None

# Defining My Functions
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

def create_app_ui():
    # Create the UI of the Webpage here
    main_layout = html.Div(
    [
    html.H1(children='Sentiments Analysis with Insights', id='Main_title'),
    html.Button(children='Find Review', id='button_review',n_clicks=0)
    ]
    )
    
    return main_layout


'''
you need to call this function , when someone clicks the button
parameter and return 
Wiring   when someone click .. call update_app_ui 
callbacks  -- jadooo  - magic   
paramter to my function  ==== Input
return of my function ==== Output
Decorators
'''

@app.callback(
    Output('button_review', 'children'),
    [
    Input('button_review', 'n_clicks')
    ]
    )
def update_app_ui(n_clicks):
    print("Value passed when clicked on button close = ", str(n_clicks))
    if (n_clicks > 0):
      return "I do not know : " + str(n_clicks)
    else:
      return "Click to Test"
    
    
# Main Function to control the Flow of your Project
def main():
    load_model()
    
    open_browser()
    
    global project_name
    project_name = 'Sentiments Analysis with Insights'
      
    global app
    app.title = project_name
    app.layout = create_app_ui()
    app.title = project_name
    # go to https://www.favicon.cc/ and download the ico file and store in assets directory 
    app.run_server() # debug=True
  
    print("This would be executed only after the script is closed")
    app = None
    project_name = None

# Calling the main function 
if __name__ == '__main__':
    main()




