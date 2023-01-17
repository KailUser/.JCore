import asyncio
import pywebio
import datetime
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import defer_call, info as session_info, run_async, run_js
import datetime
import re
import urllib.request
import base64

while True:
    user_input = input("Enter a command: ")
    if user_input == "exit":
        break
    elif " " in user_input:
        command = user_input.split()
        if command == "time":
            current_time = datetime.datetime.now().time()
            print(current_time)
        elif command == "day":
            current_day = datetime.datetime.now().strftime("%A")
            print(current_day)
        elif command == "url":
            url = user_input.split()
            if re.match(r"^https?:\/\/", url):
                with urllib.request.urlopen(url) as response:
                    page_source = response.read().decode()
                print(page_source)
            else:
                print("Invalid URL")
        elif command == "encode":
            data = user_input.split()
            encoded_data = base64.b64encode(data.encode())
            print(encoded_data)
        elif command == "decode":
            data = user_input.split()
            decoded_data = base64.b64decode(data)
            print(decoded_data.decode())
        else:
            print("Invalid command")
    else:
        print("Invalid input")




#Create KailUser(☄ S͇͇y͇͇i͇͇r͇͇e͇͇z͇͇z͇͇ ☄#2023)
