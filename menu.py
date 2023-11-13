# Remake menu.py using a class system
# Version: 1.0.1

# Import necessary libraries
import os
import keyboard
import colorama

# Function to clear the console screen
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# Class definition for the menu system
class Menu:
    def __init__(self, options, color=colorama.Fore.CYAN):
        self.options = options
        self.color = color
        self.index = 0
        self.index_max = len(options)
        self.selected = None
        self.json = {}
        self.last_known_index = 1
        self.create_menu()

    def create_menu(self):
        # Initialize colorama for colored console output
        colorama.init(autoreset=True)

        # Create a dictionary mapping index to menu options
        for option in self.options:
            self.json[self.index] = option
            self.index += 1

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
        self.index -= 1
        if self.index < 0:
            self.index = self.index_max - 1

    def down(self):
        # Move the selection index down
        self.index += 1
        if self.index >= self.index_max:
            self.index = 0

    def enter(self):
        # Set the selected option based on the current index
        self.selected = self.index

    def display(self):
        # Initialize index and selected values
        self.index = 0
        self.selected = None

        # Display the menu options with highlighting for the selected option
        while True:
            if self.selected is not None:
                # Break the loop if an option is selected
                break
            if self.last_known_index != self.index:
                # Update the screen with the current menu state
                self.last_known_index = self.index
                cls()

                for i in range(self.index_max):
                    if i == self.index:
                        print(self.color + self.json[i])
                    else:
                        print(self.json[i])

        # Set the selected value to the corresponding menu option
        self.selected = self.json[self.selected]
        return


