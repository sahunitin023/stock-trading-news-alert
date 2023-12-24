import requests
import math
import secretKey
from datetime import date

news_api_key = secretKey.NEWS_API_KEY
stocks_api_key = secretKey.STOCKS_API_KEY

STOCK = "RKLB"#To be Change
COMPANY_NAME = "Tesla Inc"

stocks_endpoint = 'https://www.alphavantage.co/query'

stockApiParams = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': stocks_api_key,
}

stocksResponse = requests.get(stocks_endpoint, params=stockApiParams)
stocksResponse.raise_for_status()
data = stocksResponse.json()['Time Series (Daily)']

closePrices = [data[i]['4. close'] for index, i in enumerate(data) if index < 2]
diff_percent = ((float(closePrices[0]) - float(closePrices[1])) / float(closePrices[1])) * 100

if diff_percent>5 or diff_percent <-5:
    print("Get News")



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

