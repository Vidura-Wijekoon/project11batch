# https://pastebin.com/DvRuRqeU
#importing the libraries
import pickle
import pandas as pd                      
import webbrowser
# !pip install dash
import dash                             
import dash_html_components as html


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
    main_layout = html.Div()
    return main_layout


# Main Function to control the Flow of your Project
def main():  
    
    load_model()
    open_browser()

    global project_name
    project_name = 'Sentiments Analysis with Insights'

    global app
    app.title = project_name
    app.layout = create_app_ui()
    app.run_server() # debug=True

    print("This would be executed only after the script is closed")
    app = None
    project_name = None

# Calling the main function 
if __name__ == '__main__':
    main()


'''
Following are the key points about the global keyword

    A variable declared outside a function is a global variable by default.

    A variable declared inside a function is local variable by default.

    We use a global keyword for a variable which is inside a function 
    so that it can be modified.
    
    Global is used to create global variables from a non-global scope 
    i.e inside a function.
    
'''