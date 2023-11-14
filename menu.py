# Remake menu.py using a class system
# Version: 1.0.2

# Import necessary libraries
import os
import keyboard

# Class definition for the menu system
class Menu:
    def __init__(self, options, color='\033[36m'):  # Use ANSI escape code for color
        self.options = options
        self.color = color
        self.index = 0
        self.index_max = len(options)
        self.selected = None
        self.json = {}
        self.last_known_index = 1
        self.create_menu()

    def create_menu(self):
        # Create a dictionary mapping index to menu options
        for index, option in enumerate(self.options):
            self.json[index] = option

        # Set up hotkeys for navigation
        keyboard.add_hotkey('up', self.up, suppress=True)
        keyboard.add_hotkey('down', self.down, suppress=True)
        keyboard.add_hotkey('enter', self.enter, suppress=True)
        keyboard.add_hotkey('right', self.enter, suppress=True)

        # Display the menu and wait for user input
        self.display()

        # Unhook all hotkeys after menu display
        keyboard.unhook_all()
        return self.selected

    def up(self):
        # Move the selection index up
        self.index = (self.index - 1) % self.index_max

    def down(self):
        # Move the selection index down
        self.index = (self.index + 1) % self.index_max

    def enter(self):
        # Set the selected option based on the current index
        self.selected = self.index

    def display(self):
        # Initialize index and selected values
        self.index = 0
        self.selected = None

        # Display the menu options with highlighting for the selected option
        while self.selected is None:
            if self.last_known_index != self.index:
                # Update the screen with the current menu state
                self.last_known_index = self.index
                self.cls()

                for i in range(self.index_max):
                    if i == self.index:
                        print(self.color + self.json[i] + '\033[0m')
                    else:
                        print(self.json[i])

        # Set the selected value to the corresponding menu option
        self.selected = self.json[self.selected]

    @staticmethod
    def cls():
        # Clear the console screen
        os.system('cls' if os.name == 'nt' else 'printf "\033c"')



