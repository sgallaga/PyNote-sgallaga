# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Santiago Gallaga-Rabinowitz
# sgallaga@uci.edu

import json, time, Profile
from collections import namedtuple


# Namedtuple to hold the values retrieved from json messages.
# TODO: update this named tuple to use DSP protocol keys
DataTuple = namedtuple('DataTuple', ['d_type','d_msg','d_token'])
d_token = "None"
k_profile = Profile.Profile()

def extract_json(json_msg:str) -> DataTuple:
  '''
  Call the json.loads function on a json string and convert it to a DataTuple object
  
  TODO: replace the pseudo placeholder keys with actual DSP protocol keys
  '''
  global d_token
  
  try:
    json_obj = json.loads(json_msg)
    d_type = json_obj['response']['type']
    d_msg = json_obj['response']['message']

    if d_type == "ok":
      try:
        d_token = json_obj['response']['token']

      except KeyError:
        pass
  except json.JSONDecodeError:
    print("Json cannot be decoded.")

  return DataTuple(d_type, d_msg, d_token)

def join(usr:str, pswrd:str):

  """
  Returns a join request in proper DS format
  """
  return '{{\"join\": {{\"username\": \"{key_1}\", \"password\": \"{key_2}\", \"token\":\"\"}}}}'.format(key_1 = usr, key_2 = pswrd)


def post(key: str):
  """
  Takes key from args, and receives a copy of profile being used, and then selects appropriate post based on key to pack into JSON format
  """
  
  global d_token
  global k_profile
  post_obj = k_profile.get_posts()[int(key)]
  d_entry = post_obj.get_entry()
  d_time = post_obj.get_time()
  #print('{{\"token\":\"{token}\", \"post\": {{\"entry\": \"{entry}\",\"timestamp\": \"{time}\"}}}}'.format(token = d_token, entry = d_entry, time = d_time))
  
  return '{{\"token\": \"{token}\", \"post\": {{\"entry\": \"{entry}\",\"timestamp\": \"{time}\"}}}}'.format(token = d_token, entry = d_entry, time = d_time)

def bio(bio: str):
  """
  Converts bio args into JSON format to send to the server
  """
  
  global d_token
  timestamp = time.time()
  print('{{\"token\": \"{token}\", \"post\": {{\"entry\": \"{entry}\",\"timestamp\": \"{time}\"}}}}'.format(token = d_token, entry = bio, time = timestamp))

  return '{{\"token\": \"{token}\", \"post\": {{\"entry\": \"{entry}\",\"timestamp\": \"{time}\"}}}}'.format(token = d_token, entry = bio, time = timestamp)
