# Install yfinance requests beautifulsoup4 pandas plotly 
import yfinance as yf

import pandas as pd

import requests

from bs4 import BeautifulSoup

import plotly.graph_objects as go

from plotly.subplots import make_subplots 

# Defining function to create stock and revenue dashboard for Tesla and Gamestop data

def make_dashboard(stock_data, revenue_data, stock_name):

    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.05,

                        subplot_titles=("Historical Share Price", "Historical Revenue"))

    fig.add_trace(go.Scatter(x=stock_data['Date'], y=stock_data['Close'], name="Share Price"), row=1, col=1)

    fig.add_trace(go.Scatter(x=revenue_data['Date'], y=revenue_data['Revenue'], name="Revenue"), row=2, col=1)

    fig.update_layout(title=stock_name + " Stock and Revenue Dashboard", height=800, width=1000)

    fig.show()

## Extracting Tesla stock data using yfinance

tesla_stock = yf.Ticker("TSLA")

tesla_data = tesla_stock.history(period="max")

tesla_data.reset_index(inplace=True)

## Extracting Tesla revenue data using web scraping

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"

html_data = requests.get(url).text

soup = BeautifulSoup(html_data, 'html5lib')

tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for row in soup.find("tbody").find_all('tr'):

    col = row.find_all("td")

    date = col[0].text

    revenue = col[1].text

    tesla_revenue = tesla_revenue.append({"Date":date, "Revenue":revenue}, ignore_index=True)

tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")

tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

# Extracting GameStop stock data using yfinance

gme_stock = yf.Ticker("GME")

gme_data = gme_stock.history(period="max")

gme_data.reset_index(inplace=True)

# Extracting GameStop revenue data using web scraping

url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"

html_data = requests.get(url).text

soup = BeautifulSoup(html_data, 'html5lib')

gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for row in soup.find("tbody").find_all('tr'):

    col = row.find_all("td")

    date = col[0].text

    revenue = col[1].text

    gme_revenue = gme_revenue.append({"Date":date, "Revenue":revenue}, ignore_index=True)

gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"")

gme_revenue.dropna(inplace=True)

gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]

## Creating Tesla stock and revenue dashboard with function from above

make_dashboard(tesla_data, tesla_revenue, "Tesla")

# Create GameStop stock and revenue dashboard with function built above

make_dashboard(gme_data, gme_revenue, "GameStop")