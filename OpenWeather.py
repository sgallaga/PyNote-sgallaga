# openweather.py

# Starter code for assignment 4 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Santiago Gallaga-Rabinowitz
# sgallaga@uci.edu

import urllib, json
from urllib import request,error
from WebAPI import WebAPI

MY_APIKEY = '816de14d750d6dd601ecc31a5031cb82'


class OpenWeather(WebAPI):
    """
    A class that's able to take a zipcode and produce the current state of said locations's weather at the time of request
    """
    
    apikey = ""
    zipcode = ""
    ccode = ""
    url = ""

    temperature = None
    high_temperature = None
    low_temperature = None
    longitude = None
    latitude = None
    description = None
    humidity = None
    sunset = None
    city = ""

    def __init__(self, zipcode:str='94702', ccode:str='us'):
        self.zipcode = zipcode
        self.ccode = ccode
        

    def load_data(self):
        """
        First downloads json object from API service and then sets attributes according to values from said object
        """

        self.url = f"http://api.openweathermap.org/data/2.5/weather?zip={self.zipcode},{self.ccode}&appid={self.apikey}"
        weather_obj = super()._download_url(self.url)


        if weather_obj != None:
            
            self.temperature = weather_obj['main']['temp']
            self.high_temperature = weather_obj['main']['temp_max']
            self.low_temperature = weather_obj['main']['temp_min']
            self.longitude = weather_obj['coord']['lon']
            self.latitude = weather_obj['coord']['lat']
            self.description = weather_obj['weather'][0]['description']
            self.humidity = weather_obj['main']['humidity']
            self.sunset = weather_obj['sys']['sunset']
            self.city = weather_obj['name']

    def transclude(self, msg: str) -> str:
        """
        Converts keywords in message into attributes found in class instance
        """

        if self.description != None:

            #Checks message for keyword then if found replaces keyword with appropriate attribute
            
            msg_split = msg.split()
            for index, word in enumerate(msg_split):
                if word == "@weather":
                    msg_split[index] = self.description


            return ' '.join(msg_split)
            

