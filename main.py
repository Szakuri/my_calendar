from menu import *
from calendar import *

def main():
    calendar = []


    menu = Menu()

    menu.add_command(ExitCommand(menu))

    menu.run()

main()
