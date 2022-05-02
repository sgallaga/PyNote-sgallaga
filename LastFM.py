# lastfm.py

# Starter code for assignment 4 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Santiago Gallaga-Rabinowitz
# sgallaga@uci.edu


import urllib, json
from urllib import request,error
from WebAPI import WebAPI

MY_APIKEY = '02fa7b7f90a937c5351cf9a00466e0a2'

class LastFM(WebAPI):
    """
    Class made for replacing keywords in a message into data found form the LastFM API
    """

    top_art = ""
    play_count = 0
    listeners = 0
    apikey = ""
    url = ""

    def __init__(self):
        pass
    

    def load_data(self):
        """
        Loads data from downloaded object from API into instance's attributes for later transclusion
        """

        self.url = f"http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&limit=1&api_key={self.apikey}&format=json"
        last_obj = super()._download_url(self.url)

        if last_obj != None:

            self.top_art = last_obj['artists']['artist'][0]['name']
            self.play_count = last_obj['artists']['artist'][0]['playcount']
            self.listeners = last_obj['artists']['artist'][0]['listeners']

    def transclude(self, msg: str) -> str:
        """
        Takes attributes and replaces keywords with appropriate attributes
        """

        if self.top_art != None:

            #Checks for keywords within the message given and then replaces all keywords with appropriate attributes
            
            msg_split = msg.split()
            for index, word in enumerate(msg_split):
                if word == "@lastfm":
                    msg_split[index] = self.top_art

            return ' '.join(msg_split)

