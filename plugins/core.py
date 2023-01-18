import requests
from bs4 import BeautifulSoup
import os
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

        