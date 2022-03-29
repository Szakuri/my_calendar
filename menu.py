class MenuCommand:
    def description(self):
        raise NotImplementedError

    def execute(self):
        raise NotImplementedError

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