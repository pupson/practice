import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

OWM_Endpoint = 'http://api.openweathermap.org/data/2.5/onecall'
api_key = os.environ.get('OWM_API_KEY')

account_sid = 'your_account_sid'
auth_token = os.environ.get('AUTH_TOKEN')

LATITUDE = your_lat
LONGITUDE = your_lon
TWILIO_NUMBER = '+##########'
TARGET_PHONE = '+##########'

weather_params = {
    'lat': LATITUDE,
    'lon': LONGITUDE,
    'appid': api_key,
    'exclude': 'current,minutely,daily',
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
print(response.raise_for_status())
weather_data = response.json()

will_rain = False

weather_slice = weather_data['hourly'][:12]
for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
                    .create(
                         body="It's going to rain, bring an umbrella",
                         from_=TWILIO_NUMBER,
                         to=TARGET_PHONE
                     )

print(message.status)
