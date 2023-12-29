import requests
import math
from datetime import date
from sms_logic import SMSLogic
from articleModel import NewsModel

news_api_key = '69c894ea614f4f6f93f71b26bcc5902c'
stocks_api_key = 'HJ0DL7JPVAG13E6O'

STOCK = "NEO"#To be Change
COMPANY_NAME = "NeoGenomics"

stocks_endpoint = 'https://www.alphavantage.co/query'
newsapi_endpoint = 'https://newsapi.org/v2/everything'

stockApiParams = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': stocks_api_key,
}

newsapi_params = {
    'apiKey': news_api_key,
    'qInTitle': COMPANY_NAME
}

def getNews():
    newsResponse = requests.get(newsapi_endpoint,params=newsapi_params)
    newsResponse.raise_for_status()
    data = newsResponse.json()['articles']
    newsArticles = data[:3]
    return newsArticles


def send_sms(news):
    sms = SMSLogic()
    for i in range(3):
        sms.send_message(message=f"{STOCK}: {f'🔻{abs(int(diff_percent))}' if diff_percent < 0 else f'🔺{abs(int(diff_percent))}'}%\nHeadline: {news[i].headline}\nBrief: {news[i].brief}\n\n",
                         receiverNumber='+917978622820',
        )


stocksResponse = requests.get(stocks_endpoint, params=stockApiParams)
stocksResponse.raise_for_status()
data = stocksResponse.json()['Time Series (Daily)']
closePrices = [data[i]['4. close'] for index, i in enumerate(data) if index < 2]
diff_percent = ((float(closePrices[0]) - float(closePrices[1])) / float(closePrices[1])) * 100

if diff_percent>5 or diff_percent <-5:
    newsData = getNews()
    news = [NewsModel(i) for i in newsData]
    send_sms(news)




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

