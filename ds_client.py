# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Santiago Gallaga-Rabinowitz
# sgallaga@uci.edu
# 81967985

import socket
import ds_protocol

def send(server:str, port:int, username:str, password:str, message:str, bio:str=None):
  '''
  The send function joins a ds server and sends a message, bio, or both

  :param server: The ip address for the ICS 32 DS server.
  :param port: The port where the ICS 32 DS server is accepting connections.
  :param username: The user name to be assigned to the message.
  :param password: The password associated with the username.
  :param message: The message to be sent to the server.
  :param bio: Optional, a bio for the user.
  '''
  #TODO: return either True or False depending on results of required operation
  
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

    try:
      
      client.connect((server, port))

    except:

      print('Error: Socket or port doesn\'t exist')

    else:

      send = client.makefile('w')
      recv = client.makefile('r')

      print(f"client connected to {server} on {port}")
      
      send.write(ds_protocol.join(username, password))
      send.flush()

      srv_msg = ds_protocol.extract_json(recv.readline())

      if srv_msg.d_type == "error":
        print(srv_msg.d_msg)
        return False

      elif srv_msg.d_type == "ok":

        print(srv_msg.d_msg)
        
        if message != "":
          send.write(ds_protocol.post(message))
          send.flush()

          f_msg = ds_protocol.extract_json(recv.readline())
          print("Response:", f_msg.d_msg)

        if bio != None:
          send.write(ds_protocol.bio(bio))
          send.flush()

          f_msg = ds_protocol.extract_json(recv.readline())
          print("Response",f_msg.d_msg)

