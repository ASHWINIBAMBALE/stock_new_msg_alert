import requests
from twilio.rest import Client
auth_token="****************"
account_sid="****************"
API_KEY="****************"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY="****************"
NEWS_APIKEY="d08a93e6869044a7aef269ce4a0572ca"
STOCK_ENDPOINT = "https://www.alphavantage.co/query?"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
FUNCTION="TIME_SERIES_DAILY"
SYMBOL="IBM"
STOCK_PARAMETERS={
    "function":FUNCTION,
    "symbol":STOCK,
    "apikey":API_KEY
}
Q="tesla"
SORT_BY="publishedAt"

stock_response=requests.get(url=STOCK_ENDPOINT,params=STOCK_PARAMETERS)
data_stock=stock_response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data_stock.items()]
yesterday=data_list[0]
yesterday_closing_price=yesterday["4. close"]
yesterday_closing_price=(yesterday_closing_price)
day_before_yesterday=data_list[1]
day_before_yesterday_closing=day_before_yesterday["4. close"]
day_before_yesterday_closing=(day_before_yesterday_closing)
print(day_before_yesterday_closing,yesterday_closing_price)
difference=abs( float(day_before_yesterday_closing)-float(yesterday_closing_price))
diff_percent=(difference/float(yesterday_closing_price))*100
if diff_percent>3:
    print("get news")
    NEWS_PARAMETER={
        "apiKey":NEWS_APIKEY,
    "qInTitle":COMPANY_NAME,
    }
    news_response=requests.get(url=NEWS_ENDPOINT,params=NEWS_PARAMETER)
    article_news=news_response.json()["articles"]
    three_artticles=article_news[:3]
    formatted_article=[f"Headline: {article['title']}./n Brief: {article['description']}" for article in three_artticles]
    for article in formatted_article:
            client=Client(account_sid,auth_token)
            message = client.messages \
                        .create(
                            body=article,
                            from_='+14127724033',
                            to='+919167822155'
                        )
    print(message.status)


