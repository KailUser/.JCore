import os

import colorama
import pyfiglet
from colorama import Fore

from plugins import core as a

colorama.init()
options = ['Site parsing', 'Ping', 'Port Check', 'Site Status', 'Create DB', 'GitHub', 'Exit']


def display_menu():
    ascii_banner = pyfiglet.figlet_format(". J C o r e", font="5lineoblique")
    print(ascii_banner)
    print(Fore.CYAN + f'Please select an option:')
    for i, option in enumerate(options):
        print(Fore.CYAN + f'{i + 1}. {option}')


def handle_selection(selection):
    if selection == 1:
        os.system('cls')
        print(a.parser.parser())
    elif selection == 2:
        os.system('cls')
        print(a.ping.ping())
    elif selection == 3:
        os.system('cls')
        print(a.ping.check_port())
    elif selection == 4:
        os.system('cls')
        print(a.ping.check_status())
    elif selection == 5:
        print(a.DB.DB())
    elif selection == 6:
        a.GH.Git()
    elif selection == 7:
        os.system('cls')
        quit()
    else:
        print('Invalid selection')


if __name__ == '__main__':
    display_menu()
    selection = int(input(Fore.LIGHTCYAN_EX + "Selection: "))
    handle_selection(selection)
