import requests
from bs4 import BeautifulSoup
import os
import socket
import time
import sqlite3
import sys
import os
import webbrowser

class parser():
    def parser():
        url = input("Enter the URL: ")
        element = input("Enter the element you want to find: ")

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all elements matching the input
        elements = soup.find_all(element)
        for e in elements:
            os.system("cls")
            print(e)
class ping():
    def ping():
        Host = input("Host for ping: ")
        Ping = os.system("ping /n 10 /l 50 /w 20000  " + Host)
    def check_port():
        host = input("Enter the host URL: ")
        port = int(input("Enter the port number: "))
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f'Port {port} is open on host {host}')
            else:
                print(f'Port {port} is closed on host {host}')
            sock.close()
        except socket.gaierror:
            print(f'Cannot resolve host: {host}')
        except socket.error:
            print(f'Cannot connect to host: {host}')
    def check_status():
        url = input("Enter the URL: ")
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f'{url} is up and running')
            else:
                print(f'{url} returned status code {response.status_code}')
        except requests.exceptions.RequestException as e:
            print(f'{url} is down. Reason: {e}')
class DB():
    def DB():
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
class GH():
    def Git():
        webbrowser.open("https://github.com/KailUser/.JCore")