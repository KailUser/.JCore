import webbrowser
import colorama
import sys
import os
import time
import sqlite3
from plugins import core as a
from colorama import Fore, Back, Style

colorama.init()
options = ['Site parsing', 'Ping' , 'Create DB' ,'GitHub', 'Exit']

def display_menu():
    print('Please select an option:')
    for i, option in enumerate(options):
            print(Fore.RED + f'{i+1}. {option}')


def handle_selection(selection):
    if selection == 1:
        os.system('cls')
        print(a.parser.parser())
    elif selection == 2:
        os.system('cls')
        print(a.ping.ping())
    elif selection == 3:
        os.system('cls')
        print("Creating DB...")
        #connect to or create a new database
        conn = sqlite3.connect(f'main.db')
        time.sleep(1)
        #create a cursor object
        cursor = conn.cursor()
        print("Create table")
        #create a table
        cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
        time.sleep(1)
        #commit the changes
        print("Commit changes")
        conn.commit()
        #close the connection
        time.sleep(2)
        print("Close connection")
        conn.close()
        os.system("cls")
        sys.exit()
    elif selection == 4:
        os.system('cls')
        webbrowser.open("https://github.com/KailUser/.JCore")
    elif selection == 5:
        os.system('cls')
        quit()
    else:
        print('Invalid selection')

if __name__ == '__main__':
    display_menu()
    selection = int(input())
    handle_selection(selection)
