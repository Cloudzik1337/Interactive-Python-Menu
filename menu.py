# Remake menu.py using a class system
# Version: 1.0.3

# Import necessary libraries
import os
import keyboard
from pystyle import Center

class Colors:
    ENDC: str = '\033[0m'
    BOLD: str = '\033[1m'
    UNDERLINE: str = '\033[4m'
    BLACK: str = '\033[30m'
    RED: str = '\033[31m'
    GREEN: str = '\033[32m'
    YELLOW: str = '\033[33m'
    BLUE: str = '\033[34m'
    MAGENTA: str = '\033[35m'
    CYAN: str = '\033[36m'
    WHITE: str = '\033[37m'
    REDBG: str = '\033[41m'
    GREENBG: str = '\033[42m'
    YELLOWBG: str = '\033[43m'
    BLUEBG: str = '\033[44m'
    MAGENTABG: str = '\033[45m'
    CYANBG: str = '\033[46m'
    WHITEBG: str = '\033[47m'
    GREY: str = '\033[90m'
    REDGREY: str = '\033[91m'
    GREENGREY: str = '\033[92m'
    YELLOWGREY: str = '\033[93m'
    BLUEGREY: str = '\033[94m'
    MAGENTAGREY: str = '\033[95m'
    CYANGREY: str = '\033[96m'
    WHITEGREY: str = '\033[97m'
    GREYBG: str = '\033[100m'
    REDGREYBG: str = '\033[101m'
    GREENGREYBG: str = '\033[102m'
    YELLOWGREYBG: str = '\033[103m'
    BLUEGREYBG: str = '\033[104m'
    MAGENTAGREYBG: str = '\033[105m'
    CYANGREYBG: str = '\033[106m'
    WHITEGREYBG: str = '\033[107m'
Colors = Colors() 
    
    






# Class definition for the menu system
class Menu:
    def __init__(self, options, color=Colors.CYAN, style=1):  # Use ANSI escape code for color
        """
        :style: 1 = default, 2 = > option < style 11 = 1 but with a centered title 22 = 2 but with a centered title
        :options: list of menu options format: ["Option 1", "Option 2", "Option 3"]
        :color: ANSI escape code for color format: Colors.CYAN
        To get the selected option, use menu.selected or menu.selected_index
        """
        self.style = style
        self.options = options
        self.color = color
        self.index = 0
        self.index_max = len(options)
        self.selected = None
        self.json = {}
        self.last_known_index = 1
        self._create_menu()

    def _create_menu(self):
        # Create a dictionary mapping index to menu options
        for index, option in enumerate(self.options):
            self.json[index] = option

        # Set up hotkeys for navigation
        keyboard.add_hotkey('up', self._up, suppress=True)
        keyboard.add_hotkey('down', self._down, suppress=True)
        keyboard.add_hotkey('enter', self._enter, suppress=True)
        keyboard.add_hotkey('right', self._enter, suppress=True)

        # Display the menu and wait for user input
        self._display()

        # Unhook all hotkeys after menu display
        keyboard.unhook_all()
        return self.selected

    def _up(self):
        # Move the selection index up
        self.index = (self.index - 1) % self.index_max

    def _down(self):
        # Move the selection index down
        self.index = (self.index + 1) % self.index_max

    def _enter(self):
        # Set the selected option based on the current index
        self.selected = self.index
    
    def _style_parse(self):
        """ Parse the style and display the menu
        1 = default, 
        2 = > option < style 
        11 = 1 but with a centered title 
        22 = 2 but with a centered title
        """
        if self.style == 1:
            for i in range(self.index_max):
                if i == self.index:
                    print(self.color + self.json[i] + Colors.ENDC)
                else:
                    print(self.json[i])
        elif self.style == 2:
            for i in range(self.index_max):
                if i == self.index:
                    print(self.color + "> " + self.json[i] + " <" + Colors.ENDC)
                else:
                    print(self.json[i])
        elif self.style == 11:
            for i in range(self.index_max):
                if i == self.index:
                    print(Center.XCenter(self.color + self.json[i] + Colors.ENDC))
                else:
                    print(Center.XCenter(self.json[i]))
        elif self.style == 22:
            for i in range(self.index_max):
                if i == self.index:
                    #blank space for centering
                    print(Center.XCenter(self.color + "         > " + self.json[i] + " <" + Colors.ENDC))
                else:
                    print(Center.XCenter(self.json[i]))


    def _display(self):
        
        # Initialize index and selected values
        self.index = 0
        self.selected = None

        # Display the menu options with highlighting for the selected option
        while self.selected is None:
            if self.last_known_index != self.index:
                # Update the screen with the current menu state
                self.last_known_index = self.index
                self.cls()
                self._style_parse()
                    
        # Set the selected value to the corresponding menu option
        self.selected = self.json[self.selected]
        self.selected_index = self.index

    @staticmethod
    def cls():
        # Clear the console screen
        os.system('cls' if os.name == 'nt' else 'printf "\033c"')

# Example usage:

# options = ["Style1", "Option 2", "Option 3", "Option 4", "Option 5"]
# menu = Menu(options, Colors.CYAN, 1)
# print("Selected option:", menu.selected)

# options = ["Style2", "Option 2", "Option 3", "Option 4", "Option 5"]
# menu = Menu(options, Colors.CYAN, 2)
# print("Selected option:", menu.selected)

# options = ["Style11", "Option 2", "Option 3", "Option 4", "Option 5"]
# menu = Menu(options, Colors.CYAN, 11)
# print("Selected option:", menu.selected)

# options = ["Style22", "Option 2", "Option 3", "Option 4", "Option 5"]
# menu = Menu(options, Colors.CYAN, 22)
# print("Selected option:", menu.selected)


