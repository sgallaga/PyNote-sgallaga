# a4.py

# Starter code for assignment 4 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Santiago Gallaga-Rabinowitz
# sgallaga@uci.edu
# 81967985


from Profile import Profile, Post, DsuFileError, DsuProfileError
from pathlib import Path
from LastFM import LastFM
from OpenWeather import OpenWeather
from WebAPI import WebAPI
import ds_client, ds_protocol

#recursive list function global variables
r_list = []
s_list = []
e_list = []
counter = 0
key_profile = Profile()
active_path = ''
port = 3021

def run():
    active_program = True
    while active_program:
        user_input = input()
        user_list = user_input.split()
        command_k = user_list[0]

        if len(user_list) > 1:
            t = Path(user_list[1])
            if t.exists():
                
                if command_k == 'L':
                    if len(user_list) <= 2:
                        file_list(user_list[1], None)
                    else:
                        file_list(user_list[1], user_list[2:])

                elif command_k == 'R':
                    read_func(user_list[1])

                elif command_k == 'C':
                    create_func(user_list[1], user_list[2:])

                elif command_k == 'D':
                    delete_func(user_list[1])

                elif command_k == 'O':
                    open_func(user_list[1])

            elif command_k == 'E':
                edit_func(user_input)

            elif command_k == 'P':
                print_func(user_input)

            elif command_k == 'S':
                server_func(user_input)
                                
            else:
                print('ERROR')

        elif command_k == 'Q':
            active_program = False
            print('Programming quitting...')
        
        else:
            print('ERROR')


def print_msg(msg: str):
    print(msg)
        

def file_list(directory, optional:list)-> str:
    """
    General method that translates user input into various options and methods for the list method
    """
    global r_list
    global s_list
    global e_list
    global counter
    r_list = []
    s_list = []
    e_list = []
    counter = 0
    if optional == None:
        lst_print(iterate_dir(directory))

    
        
    elif optional[0] == '-r':
        if len(optional) > 1:
            if '-f' in optional:
                r_iterate_dir(directory)
                for path in r_list:
                    if path.is_file():
                        print(path)
            if '-s' in optional[1:]:
                r_iterate_dir(directory)
                index = optional.index('-s') + 1
                lst_print(s_search(optional, index))
            if '-e' in optional[1:]:
                r_iterate_dir(directory)
                index = optional.index('-e') + 1
                lst_print(e_search(optional, index))
            
        else:
            lst_print(r_iterate_dir(directory))
                        
    elif optional[0] == '-f':
        f_filter(directory)

    elif optional[0] == '-s':
        iterate_dir(directory)
        lst_print(s_search(optional, 1))

    elif optional[0] == '-e':
        iterate_dir(directory)
        lst_print(e_search(optional, 1))
        
        

def iterate_dir(dd)-> list:
    """
    Iterates through target directory and returns a list of all files and directories
    """
    global r_list
    p_path = Path(dd)
    for obj in p_path.iterdir():
        if obj.is_file():
            r_list.append(obj)
    for obj in p_path.iterdir():
        if obj.is_dir():
            r_list.append(obj)

    return(r_list)


def r_iterate_dir(dd)-> str:
    """
    Recursively iterates through target directory and returns a list of all files and directories found
    """

    p_path = Path(dd)
    global r_list
    for obj in p_path.iterdir():
        if obj.is_file():
            r_list.append(obj)

    for obj in p_path.iterdir():
        if obj.is_dir():
            r_list.append(obj)
            r_iterate_dir(obj)

    return(r_list)


def f_filter(dd):
    """
    Prints all objects given after a list method that are specifically files, not directories
    """
    p_path = Path(dd)
    try:
        for obj in p_path.iterdir():
            if obj.is_file():
                print(obj)
                
    except FileNotFoundError:
        print('ERROR')

def lst_print(lst:list)-> str:
    """
    Iterates through a target list and prints each element
    """

    if type(lst) == list:
        for element in lst:
            print(element)

def s_search(optional:list, appendix:int):
    """
    Returns a target file after a directory has already had the list method used on targeted directory
    """
    global r_list
    global s_list
    global counter
    if len(optional) > appendix:
        if optional[appendix] not in ('-f' , '-e'):
            for element in r_list:
                lst_atta = element.parts
                if lst_atta[-1] == optional[appendix]:
                    s_list.append(element)
                    counter += 1

            if counter == 0:
                
                print('ERROR')

            else:
                    
                return s_list
        else:
            print('ERROR')
            
    else:
        print('ERROR')

def e_search(optional:list, appendix:int):
    """
    Returns a list of files with targeted suffix
    """
    global r_list
    global e_list
    global counter
    if len(optional) > appendix:
        if optional[appendix] not in ('-s', '-f'):
            for element in r_list:
                lst_atta = element.suffix
                if lst_atta[1:] == optional[appendix]:
                    e_list.append(element)
                    counter += 1

            if counter == 0:
                print('ERROR')

            else:
                       
                return e_list
        
        else:
            print('ERROR')
            
    else:
        print('ERROR')

def read_func(dd):
    """
    Prints all decoded contents within target file
    """
    p = Path(dd)
    if p.is_file():
        if p.suffix == '.dsu':
            if p.read_text() == '':
                print('EMPTY')
            else:
                f = p.open()
                print(f.read(), end='')
                f.close()
        else:
            print('ERROR')
    else:
        print('ERROR')

def create_func(dd, optional:list):
    """
    Creates a file with a specified name within a targeted directory
    """
    global r_list
    global key_profile
    global active_path
    if len(optional) > 1:

        #Creates actual .dsu file
        ot = str(optional[1]) + '.dsu'
        p = Path(dd) / ot

        # Checks the validity of username and password
        server_name = input('Please enter server IP: ')

        if server_name != '' and ' ' not in server_name and type(server_name) == str:
            
            usr_name = input('Please enter your username: ')
            
            if usr_name != '' and ' ' not in usr_name:
                
                pswrd = input('Please enter your password: ')

                if pswrd != '' and ' ' not in pswrd:
                    
                    bio = input('Please create your bio: ')

                    if not p.exists():

                        if optional[0] == '-n':
                            
                            p.touch()
                            r_list = []
                            #Print final file
                            iterate_dir(dd)
                            for element in r_list:
                                temp = Path(element)
                                if temp.samefile(p):
                                    print(temp)                  

                            #Create
                            temp_p = Profile(server_name, usr_name, pswrd)
                            temp_p.bio = bio
                            temp_p.save_profile(str(p))
                            key_profile = temp_p
                            active_path = str(p)
                            return True

                        else:
                            print_msg('ERROR')

                    else:
                        #Loads file if file already exists
                        print_msg('File already exists; loading profile...')
                        open_func(str(p))
                        return False             

                else:
                    print_msg('Passwords can\'t contain any whitespace.')
                    return False

            else:
                print_msg('Usernames can\'t contain any whitespace.')
                return False

        else:
            print_msg('Enter proper server IP address')
            return False
                    
    else:
        print('ERROR')

def delete_func(dd):
    """
    Deletes a target file
    """
    p = Path(dd)

    if p.is_file():
        
        p.unlink()
        print(dd + ' DELETED')

    else:
        print('ERROR')

def open_func(path: str):
    """
    Opens a file
    """
    global key_profile
    global active_path
    p = Path(path)

    if p.exists():
        if p.is_file() and p.suffix == '.dsu':
            key_profile = Profile()
            key_profile.load_profile(p)
            active_path = path
            print_msg(f'Profile has been loaded...\nUsername: {key_profile.username}')

        else:
            print_msg('ERROR: object isn\'t an appropriate file')

    else:
        print_msg('ERROR: file doesn\'t exist')


def edit_func(targets: str):
    """
    Function that modifies the attributes given a path
    """
    
    global key_profile
    global active_path
    keys = []
    text = []
    del_l = []
    api_dic = {'@lastfm' : '02fa7b7f90a937c5351cf9a00466e0a2', '@weather' : 'b5ad93f735eb4d1c231727fa177d5d16'}
    api_true = False
    # Seperates text into a list of option choices and said option's replacement
    
    for optional in targets[1:].split():
        if optional[:1] == '-' and optional != '-delpost':
            keys.append(optional)
                        

    for optional in targets[1:].split('"')[1::2]:
        if optional[:1] != '-':
            text.append(optional)


    for index in range(0, len(targets[1:].split())):
        if targets[1:].split()[index] == '-delpost':
            try:
                int(targets[1:].split()[index + 1])

            except ValueError:
                print_msg('Error: index given isn\'t a number')

            else:
                del_l.append(int(targets[1:].split()[index + 1]))


    # Checks for which attributes to choose
    
    for index in range(0, len(keys)):
        if keys[index] == '-usr':
            key_profile.username = text[index]

        elif keys[index] == '-pwd':
            key_profile.password = text[index]

        elif keys[index] == '-bio':
            key_profile.bio = text[index]

        elif keys[index] == '-addpost':
            end_msg = text[index]
            a_list = end_msg.split()
            

            #Checks for any api keywords within the post first, and transcludes said keywords before creating post
            
            if '@lastfm' in a_list:
                lfm = LastFM()
                end_msg = do_api(msg, api_dic['@lastfm'], lfm)

            if '@weather' in a_list:
                zipcode = input('Enter the zipcode of desrired location: ')
                ow = OpenWeather(zipcode)
                end_msg = do_api(end_msg, api_dic['@weather'], ow)
                
                    
            post_t = Post(end_msg)
            key_profile.add_post(post_t)

        else:
            print_msg('Invalid command')

    # Generates a look-up table in order to perform multiple delete requests in a single command line

    nav = []
    nav_count = 0
    for val in key_profile.get_posts():
        nav.append(nav_count)
        nav_count += 1

    for target in del_l:
        for index, number in enumerate(nav):
            if number == target:
                key_profile.del_post(index)
                nav.pop(index)
                

    key_profile.save_profile(active_path)

def print_func(targets: str):
    global key_profile
    keys = []
    post_l = []

    # Separates command line into function calls with the post function's index inputs being placed in a list
    
    for optional in targets[1:].split():
        if optional[:1] == '-':
            keys.append(optional)

    # Separates post prompts separately then deletes later after other functions have been processed

    for index in range(0, len(targets[1:].split())):
        if targets[1:].split()[index] == '-post':
            try:
                int(targets[1:].split()[index + 1])

            except ValueError:
                print_msg('Error: index given isn\'t a number')

            else:
                post_l.append(int(targets[1:].split()[index + 1]))

    # Conditionals 

    for func in keys:
        if func == '-usr':
            print_msg(f'{key_profile.username}\n')

        elif func == '-pwd':
            print_msg(f'{key_profile.password}\n')

        elif func == '-bio':
            print_msg(f'{key_profile.bio}\n')

        elif func == '-posts':
            for index, post_obj in enumerate(key_profile.get_posts()):
                print_msg(f'[{index}]: {post_obj.get_entry()}')
            print()

        elif func == '-post':
            print_msg(f'[{post_l[0]}]: {key_profile.get_posts()[post_l[0]].get_entry()}\n')
            post_l.pop(0)

        elif func == '-all':
            print_msg(f'Username: {key_profile.username}\n')
            print_msg(f'Password: {key_profile.password}\n')
            print_msg(f'Bio: {key_profile.bio}\n')
            print_msg('Posts:\n')

            for index, post_obj in enumerate(key_profile.get_posts()):
                print_msg(f'[{index}]: {post_obj.get_entry()}')
            print()


def server_func(user_input: str):

    """
    Function used to send posts and updated bios to the ICS 32 Distributed Social
    """
    
    rig = user_input.split()
    key = None
    global key_profile
    global port

    #checks for first integer from user input

    for element in rig:
        try:
            test = int(element)

        except ValueError:
            pass

        else:
            key = test
            break

    #Validates user input before attempting to send data

    if key == None and "-bio" not in rig:
        print_msg("Enter a valid post ID or \"-bio\"")

    else:

        if key != None:

            try:
                select_post = key_profile.get_posts()[key]

            except IndexError:
                print_msg('This post doesn\'t exist')

            else:
                client_send(key)

        if "-bio" in rig:
            if not(len(user_input.split('"')) >= 2):
                print_msg("Enter valid entry after bio in quotation marks")

            else:
                new_bio = user_input.split('"')[1]
                client_send("", new_bio)
                edit_func(f'-bio "{new_bio}"')
                

                

                
def client_send(key: str, bio: str = None):
    """
    Function that sends a message to the server using separate modules
    """
    global key_profile

    
    dsuserver = key_profile.dsuserver
    usr = key_profile.username
    pswrd = key_profile.password
    ds_protocol.k_profile = key_profile
    ds_client.send(dsuserver, port, usr, pswrd, key, bio)


def do_api(message: str, apikey: str, webapi: WebAPI):

    webapi.set_apikey(apikey)
    webapi.load_data()
    new_msg = webapi.transclude(message)

    return new_msg
            

if __name__ == '__main__':
    
    run()


