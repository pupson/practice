import requests
from datetime import date
from datetime import timedelta
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
API_KEY = '####'
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = '####'

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'TSLA',
    'apikey': API_KEY,
}

news_params = {
    'qInTitle': COMPANY_NAME,
    'apiKey': NEWS_API_KEY,
}

today = date.today()
yesterday = today - timedelta(days = 1)
day_before_yesterday = today - timedelta(days = 2)

account_sid = '####'
auth_token = '####'

TWILIO_NUMBER = '+####'
TARGET_PHONE = '+####'
RECOVERY_CODE = '####'

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
#

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()['Time Series (Daily)']

yesterday_close = float(response.json()['Time Series (Daily)'][str(yesterday)]['4. close'])
print(yesterday_close)


# data_lst = [value for (key, value) in data.items()]
# yesterday_data = data_lst[0]
# yesterday_closing_price = yesterday_data['4. close']
# print(yesterday_closing_price)

#TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday_close = float(response.json()['Time Series (Daily)'][str(day_before_yesterday)]['4. close'])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

delta_price = abs(yesterday_close - day_before_yesterday_close)

delta_diff = yesterday_close - day_before_yesterday_close

up_down = None

if delta_diff > 0:
    up_down = '🔺'
else:
    up_down = '🔻'


#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percent_delta = round((delta_diff/day_before_yesterday_close)*100)



#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").


#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()

news_data = news_response.json()['articles'][:3]

# print(news_data)

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

articles = [f"{STOCK_NAME}: {up_down}{percent_delta}% \nHeadline: {article['title']} \n Description{article['description']}" for article in news_data]

#TODO 9. - Send each article as a separate message via Twilio. 


if abs(percent_delta) < 5:
    client = Client(account_sid, auth_token)
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    # client = Client(account_sid, auth_token, http_client=proxy_client)
    for article in articles:
        message = client.messages.create(
                             body=article,
                             from_=TWILIO_NUMBER,
                             to=TARGET_PHONE
                         )

print(message.status)

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

