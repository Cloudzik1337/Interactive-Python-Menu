
# Version: 1.0.4




"""

                                                                                          > Cloudzik <
                                                                                     Interactive-Python-Menu
                                                                                             1.0.4
                                                                                           15.11.2023
                                                                     https://github.com/Cloudzik1337/Interactive-Python-Menu
"""







# Import necessary libraries
import os
import keyboard
from pystyle import Center
# Class definition for the menu colors
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

# Class definition for the menu styles
class Styles:
    DEFAULT: int = 1
    SELECTED: int = 2
    ARROW: int = 3
    CENTERED: int = 11
    CENTEREDSELECTED: int = 22
    ARROWCENTERED: int = 33
    



# Create instances of the classes
Colors = Colors()  
Styles = Styles()






# Class definition for the menu system
class Menu:
    def __init__(self, options, color=Colors.CYAN, style=Styles.DEFAULT, pretext=None):  # Use ANSI escape code for color
        """
        
        :options: list of menu options format: ["Option 1", "Option 2", "Option 3"]
        :color: ANSI escape code for color format: Colors.CYAN
        :style: menu style format: Styles.DEFAULT or Styles.SELECTED or Styles.CENTERED or Styles.CENTEREDSELECTED
        :pretext: text to display before the menu otherwise it will earesed
        To get the selected option, use menu.selected or menu.selected_index

        """
        self.pretext = str(pretext)
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
        3 = ↳ option style
        11 = 1 but with a centered title 
        22 = 2 but with a centered title
        33 = 3 but with a centered title
        """
        if self.style == 1:
            parsed_chosen = "print(self.color  + self.json[self.index] + Colors.ENDC)"
            parsed = "print(self.json[i])"
            self._print_menu(parsed, parsed_chosen)
        elif self.style == 2:
            parsed_chosen = "print(self.color + '> ' + self.json[self.index] + ' <' + Colors.ENDC)"
            parsed = "print(self.json[i])"
            self._print_menu(parsed, parsed_chosen)
        elif self.style == 3:
            parsed_chosen = "print(self.color + '↳ ' + self.json[self.index] + Colors.ENDC)"
            parsed = "print(self.json[i])"
            self._print_menu(parsed, parsed_chosen)
        elif self.style == 11:
            parsed_chosen = "print(Center.XCenter(self.color + '          ' + self.json[self.index] +  Colors.ENDC))"
            parsed = "print(Center.XCenter(self.json[i]))"
            self._print_menu(parsed, parsed_chosen, center=True)
        elif self.style == 22:
            parsed_chosen = "print(Center.XCenter(self.color + '         > ' + self.json[self.index] + ' <' + Colors.ENDC))"
            parsed = "print(Center.XCenter(self.json[i]))"
            self._print_menu(parsed, parsed_chosen, center=True)
        elif self.style == 33:
            parsed_chosen = "print(Center.XCenter(self.color + '         ↳ ' + self.json[self.index] + Colors.ENDC))"
            parsed = "print(Center.XCenter(self.json[i]))"
            self._print_menu(parsed, parsed_chosen, center=True)


    def _print_menu(self, parsed, parsed_chosen, center=False):
        """By doing this i belive that i have made the code more readable and easier to understand"""
        if self.pretext != None:
            if center == True:print(Center.XCenter(self.pretext))
            else:print(self.pretext)
        for i in range(self.index_max):
            if i == self.index:
                exec(parsed_chosen)
            else:
                exec(parsed)


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



