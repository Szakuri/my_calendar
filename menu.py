class MenuCommand:
    def description(self):
        raise NotImplementedError
    print("""
       1. New event
       2. List calendar
       3. Export calendar to iCalendar
       4. Exit
       """)
    option = input("Select menu item (1-4): ")

    def execute(self):
        raise NotImplementedError
    if option == 1:
        print("Siema")



class ExitCommand(MenuCommand):
    def __init__(self, menu):
        ...
    
    def description(self):
        return "Wyjście"

    def execute(self):
        ...

class Menu:
    def __init__(self):
       ...

    def add_command(self, cmd):
        ...

    def run(self):
       ...

    def stop(self):
        ...

    def _display_menu(self):
        ...

    def _execute_selected_command(self):
        cmd_num = ...

        cmd = ...
        cmd.execute()