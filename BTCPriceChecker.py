#https://grantslattery.pythonanywhere.com/
#https://www.pythonanywhere.com/user/grantslattery/.../mysite/flask_app.py

import dash
from dash import dcc
from dash import html

import pandas as pd
import requests

bitcoin_api_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
response = requests.get(bitcoin_api_url)
response_json = response.json()

#First round of raw data cleaning
priceData = response_json.get("bpi")
timeStamp = response_json.get("time")


#Create Dash Table Data Frame with priceData variable
newpdFrame = pd.DataFrame(data=priceData)
usdData = priceData.get("USD")
gbpData = priceData.get("GBP")
eurData = priceData.get("EUR")

usdBtcPrice = usdData.get("rate")
gbpBtcPrice = gbpData.get("rate")
eurBtcPrice = eurData.get("rate")

usaTime = timeStamp.get("updated")
isoTime = timeStamp.get("updatedISO")
ukTime = timeStamp.get("updateduk")

# for deployment, pass app.server (which is the actual flask app) to WSGI etc
app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='BTC Currency Converter', 
style={'textAlign': 'center','color': 'lime'}
),

    html.Div(children='''
        Python application that converts the cost of Bitcoin to multiple currencies.
    ''',
style={'textAlign': 'center','color': 'black'}
),
    html.Div(children='''
        API & Data: CoinDesk: https://www.coindesk.com/price/bitcoin
    ''',
style={'textAlign': 'center','color': 'black'}
),


    html.H1(children="Cost of Bitcoin:", style={
            'textAlign': 'center',
            'color': 'lime'
        }),


  


    html.H2(children="$" + usdBtcPrice + " USD", style={'textAlign': 'center','color': 'black'}
),


    html.H2(children="£" + gbpBtcPrice + " GBP", style={'textAlign': 'center','color': 'black'}
),


    html.H2(children="€" + eurBtcPrice + " EUR", style={'textAlign': 'center','color': 'black'}
),

  html.H4(children="Updated: ["+usaTime +" / "+ ukTime +" / "+ isoTime+"]", 
style={'textAlign': 'center','color': 'black'}
),



])

print("Program running")


if __name__ == '__main__':
    app.run_server(debug=True)

