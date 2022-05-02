# webapi.py

# Starter code for assignment 4 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Santiago Gallaga-Rabinowitz
# sgallaga@uci.edu
# 81967985

from abc import ABC, abstractmethod
import urllib, json
from urllib import request,error

class WebAPI(ABC):
  """
  Base class for all API's used in main program; includes downloading url's and setting API keys for respective api
  """

  def _download_url(self, url_to_download: str) -> dict:
    """
    Requests data packed in JSON for eventual load method
    """
    response = None
    r_obj = None

    try:
        response = urllib.request.urlopen(url_to_download)
        json_results = response.read()
        r_obj = json.loads(json_results)

    except urllib.error.HTTPError as e:
        print('Failed to download contents of URL')

        if e.code == 404:
            print('Status code: {} Resource not available on this server'.format(e.code))

        elif e.code == 401:
            print('Status code: {} Requested resource not authorized to be returned as a response'.format(e.code))

        else:
          print('Status code: {} {}'.format(e.code, e))

    except ConnectionError:
        print("Error: Failed to download contents of URL")
        print('Error: Connection interrupted')

    except urllib.error.URLError as e:

        print('Failed to download contents of URL')
        print(e)
        
    finally:
        if response != None:
            response.close()
    
    return r_obj
	
  def set_apikey(self, apikey:str) -> None:
    """
    Sets api key
    """
    self.apikey = apikey
	
  @abstractmethod
  def load_data(self):
    """
    Method will be used to load data into individual classes
    """
    pass
	
  @abstractmethod
  def transclude(self, message:str) -> str:
    """
    Will use already loaded data from the object class into text wherever a key word calls it
    """
    pass
