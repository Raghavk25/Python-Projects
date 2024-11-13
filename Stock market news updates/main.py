import requests
import smtplib

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API = "https://www.alphavantage.co/query"
STOCK_API_KEY = "Your API key"

NEWS_API = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "Your API key"

MY_EMAIL = "user@gmail.com"
MY_PASSWORD = "password"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(url = STOCK_API, params = stock_params)
response.raise_for_status()

data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_closing_price = data_list[0]["4. close"]
# Yesterday's closing price

day_before_yesterday_closing_price = data_list[1]["4. close"]
# Day before yesterday's closing price

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
upordown = None
if difference >= 0:
    upordown = "📈"
else:
    upordown = "📉"
difference = abs(difference)


diff_percent = (difference/float(day_before_yesterday_closing_price)) * 100

if diff_percent > 2:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(url = NEWS_API, params = news_params)
    articles = news_response.json()["articles"][:3]
    formatted_articles = [f"Headline: {article['title']} \nBrief: {article['description']} " for article in articles]
    for i in range(3):
        with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
            connection.starttls()
            connection.login(user = MY_EMAIL, password = MY_PASSWORD)
            connection.sendmail(
                to_addrs = MY_EMAIL,
                from_addr = MY_EMAIL,
                msg = f"Subject: {COMPANY_NAME}: {diff_percent}% {upordown}\n\n{formatted_articles[i]}"
            )





