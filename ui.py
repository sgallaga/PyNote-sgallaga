# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Santiago Gallaga-Rabinowitz
# sgallaga@uci.edu
# 81967985

import a4
from pathlib import Path

def run():
    print('Welcome to PyNote!\nWould you like to create or load a DSU file?')

    main_menu = True

    # Prompts user to either load, create, enter admin mode, and quit

    while main_menu:
        print('Type "c" to create a file or "l" to load a file or enter "q" to quit:\n')
        user_input = input()

        if user_input == 'l' or user_input == 'L':

            load_option()

        elif user_input == 'c' or user_input == 'C':

            create_option()

        elif user_input == 'admin' or user_input == 'Admin':
            print('Admin mode activated...\n')
            a3.run()

        elif user_input == 'q' or user_input == 'Q':
            print('Program quitting...')
            main_menu = False

        else:
            print('ERROR: input not recognized')
            

def in_file():
    """
    After profile has been loaded or created, asks user to edit or print using the file
    """
    
    active = True
    
    while active:
        print('\nWould you like to edit or print something in your profile?')
        print('Type "p" to print or "e" to edit "s" to publish or "b" to go back\n')
        user_input = input()

        # Print option

        if user_input == 'p' or user_input == 'P':

            print('Enter in all the desired elements you\'d like to print\n Available options:\n')

            menu = ("\"-usr\" - Prints username\n"
                    "\"-pwd\" - Prints password\n"
                    "\"-bio\" - Prints bio\n"
                    "\"-posts\" - Prints all of your profile's posts\n"
                    "\"-post [ID]\" - Prints a selected post given an ID (No quotations needed for ID)\n"
                    "\"-all\" - Prints your entire profile and posts\n")
                    

            print(menu)

            user_choice = True

            while user_choice:
                print('Enter "b" to go back or continue printing\n')
                user_t = input()
                if user_t != 'b' and user_t != 'B':
                    tell = f'P {user_t}'
                    #update when necessary
                    a4.print_func(tell)

                else:
                    user_choice = False

        # Edit option

        elif user_input == 'e' or user_input == 'E':
            print('Enter in all the desired elements you\'d like to edit/add\n')

            e_menu = ("\"-usr\" - Edit username\n"
                      "\"-pwd\" - Edit password\n"
                      "\"-bio\" - Edit bio\n"
                      "\"-addpost\" - Add a post to your profile\n"
                      "\"-delpost\" - Deletes a post given an ID (No quotations needed for ID)\n\n"
                      "KEYWORDS: Type in these specific keywords when adding a new post for automatic fill in from the system\n"
                      "\"@weather\" --- Gives current weather status \n\"@lastfm\" --- Gives current most listened to artist in America\n")

            print(e_menu)
            print('Enter commands followed by its replacement inside double quotes')
            print('Example: -addpost "Hey there" -usr "Bob"\n')

            user_choice = True

            while user_choice:
                print('Enter "b" to go back or continue editing\n')
                user_t = input()
                if user_t != 'b' and user_t != 'B':
                    tell = f'E {user_t}'
                    #update when necessary
                    a4.edit_func(tell)

                else:
                    user_choice = False

        elif user_input == 's' or user_input == 'S':
            #update when necessary
            a4.print_func('P -posts')

            s_menu = ('You\'re now in publishing mode, enter the id of'
                      ' a post you\'d like to publish or enter \"-bio\"'
                    ' followed by text in quotes to announce your new bio publicly!\n')
            print(s_menu)
            user_input = input()
            tell = f'S {user_input}'
            #update when necessary
            a4.server_func(tell)

        elif user_input == 'b' or user_input == 'B':
            active = False

def load_option():
    """
    Prompts user for loading a file
    """
    user_choice = True

    while user_choice:
        print('Enter the filepath of the file you\'d like to load: or enter \"b\" to go back\n')
        u_p = input()

        if u_p != 'b':
            p = Path(u_p)
            if p.exists():
                if p.is_file():
                    if p.suffix == '.dsu':

                        try:
                            #update when necessary
                            a4.open_func(u_p)

                        except:
                            print('Try again - That DSU file isn\'t compatible')

                        else:
                            in_file()

                    else:
                        print('Try again - That isn\'t the right file type\n')

                else:
                    print('Try again - That isn\'t a file\n')

            else:
                print('Try again - That path doesn\'t exist\n')

        else:
            user_choice = False
            
def create_option():
    """
    Prompts the user for creating a file with a new profile
    """
    user_choice = True

    # Loop for user input and checking its validity

    while user_choice:
        print('Enter the directory where you\'d like to create the file (enter b to go back):\n')
        u_p = input()

        if u_p != 'b':
            p = Path(u_p)
            if p.exists():
                if p.is_dir():
                    print('What would you like to name the file?:\n')
                    u_n = input()

                    if ' ' not in u_n and u_n != '':
                    
                        op_prep = f'-n {u_n}'
                        optional = op_prep.split()
                        #update when necessary
                        if a4.create_func(u_p, optional) == True:
                            
                            in_file()

                    else:
                        print('Try again - File name can\'t contain whitespace')

                
                else:
                    # Calls the load function if user entered in a valid DSU file
                    
                    if p.suffix == '.dsu':
                        #update when necessary
                        a4.open_func(u_p)
                        in_file()

                    else:
                        print('Try again - That isn\'t the right file type\n')

            else:
                print('Try again - That path doesn\'t exist\n')

        else:
            user_choice = False


if __name__ == '__main__':
    run()
