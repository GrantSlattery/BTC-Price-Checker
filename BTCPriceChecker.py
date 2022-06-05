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

floatUSDBtcPrice = f"{float(usdBtcPrice.replace(',', '')):.2f}" 
floatGBPBtcPrice = f"{float(gbpBtcPrice.replace(',', '')):.2f}"
floatEURBtcPrice = f"{float(eurBtcPrice.replace(',', '')):.2f}"

finalUSDBtcPrice = "{:,}".format(float(floatUSDBtcPrice))
finalGBPBtcPrice = "{:,}".format(float(floatGBPBtcPrice))
finalEURBtcPrice = "{:,}".format(float(floatEURBtcPrice))


usaTime = timeStamp.get("updated")
isoTime = timeStamp.get("updatedISO")
ukTime = timeStamp.get("updateduk")

# for deployment, pass app.server (which is the actual flask app) to WSGI etc
app = dash.Dash()

app.layout = html.Div(style={'background-color': 'gold', 'position':'absolute', 'top':'0', 'bottom':'0', 'left':'0', 'right':'0'}, children=[ 
    html.H1(children='BTC Price Checker', 
style={'textAlign': 'center','text-transform': 'uppercase',
'color': 'white', 'font-family': 'Arial, Helvetica, sans-serif',
}
),

    html.Div(children='''
        Python application that converts the price of Bitcoin to multiple currencies.
    ''',
style={'textAlign': 'center','color': 'black', 'font-family': 'Arial, Helvetica, sans-serif', 'font-size': '15px'}
),
    html.Div(children='''
        API & Data: CoinDesk (https://www.coindesk.com/price/bitcoin)
    ''',
style={'textAlign': 'center','color': 'black', 'font-family': 'Arial, Helvetica, sans-serif', 'font-size': '15px'}
),


    html.H2(children="Cost of Bitcoin:", style={
'font-size': '30px',
            'textAlign': 'center', 
		  'text-transform': 'uppercase',
            'color': 'white', 'font-family': 'Arial, Helvetica, sans-serif'
        }),


  

    html.H3(children="$" + finalUSDBtcPrice  + " USD", style={'font-size': '25px', 'textAlign': 'center','color': 'black', 'font-family': 'Arial, Helvetica, sans-serif'}
),


    html.H3(children="£" + finalGBPBtcPrice  + " GBP", style={'font-size': '25px','textAlign': 'center','color': 'black', 'font-family': 'Arial, Helvetica, sans-serif'}
),


    html.H3(children="€" + finalEURBtcPrice  + " EUR", style={'font-size': '25px','textAlign': 'center','color': 'black', 'font-family': 'Arial, Helvetica, sans-serif'}
),

  html.H4(children="Updated: ["+usaTime +" / "+ ukTime +" / "+ isoTime+"]", 
style={'font-size': '12px','textAlign': 'center','color': 'black', 'font-family': 'Arial, Helvetica, sans-serif'}
),



])

print("Program running")



if __name__ == '__main__':
    app.run_server(debug=True)



