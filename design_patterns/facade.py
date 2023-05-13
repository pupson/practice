import urllib
import urllib.parse
import urllib3


class WeatherProvider(object):

    def __init__(self, city, country):
        self.city = city
        self.country = country
        self.api_url = 'http://api.openweather.org/data/2.5/forecast?q={},{}'

    def get_weather_data(self):
        self.city = urllib.parse.quote(self.city)
        self.country = urllib.parse.quote(self.country)
        url = self.api_url.format(self.city, self.country)
        print(url)
        return urllib.request.urlopen(url).read()

w = WeatherProvider('london', 'england')
print(w.get_weather_data())