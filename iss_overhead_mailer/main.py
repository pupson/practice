import requests
import datetime as dt
import smtplib
import time

MY_LAT = 37.816994
MY_LNG = -122.120273


def iss_near():

    response = requests.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()

    data = response.json()

    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])

    iss_position = (iss_longitude, iss_latitude)

    if (MY_LAT-5) <= iss_position[0] <= (MY_LAT+5) and (MY_LNG-5) <= iss_position[1] <= -(MY_LAT+5):
        return True

def is_night():

    time_now = dt.datetime.now()
    hour_now = time_now.hour

    parameters = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0,
    }

    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    if hour_now >= sunset or hour_now >= sunrise:
        return True

def iss_mailer():
    g_email = 'email1@gmail.com'
    g_smtp = 'smtp.gmail.com'
    g_password = 'pass1'

    with smtplib.SMTP(g_smtp, port=587) as connection:
        connection.starttls()
        connection.login(user=g_email, password=g_password)
        connection.sendmail(
            from_addr=g_email,
            to_addrs='target@gmail.com',
            msg=f'Subject: ISS Overhead\n\nLook up!')

while True:
    time.sleep(60)
    if is_night() and iss_near():
        iss_mailer()




