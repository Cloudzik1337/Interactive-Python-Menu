# Import necessary libraries
import colorama
import os
import keyboard

# Initialize colorama for cross-platform colored output
colorama.init(autoreset=True)

# Define a function to clear the console screen based on the operating system
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# Initialize global variables
selected = None
index = 0

# Function to create a menu with the given options
def create_menu(options, color=colorama.Fore.CYAN):
    # Create a dictionary to store options with their corresponding index
    json = {}
    global index, index_max
    index = 0
    index_max = len(options)
    
    # Populate the dictionary with options and their indices
    for option in options:
        json[index] = option
        index += 1
    
    # Bind keys for menu navigation
    keyboard.add_hotkey('up', up, suppress=True)
    keyboard.add_hotkey('down', down, suppress=True)
    keyboard.add_hotkey('enter', enter, suppress=True)
    keyboard.add_hotkey('right', enter, suppress=True)
    
    # Display the menu and return the selected option
    to_ret = display(json, color)
    keyboard.unhook_all()
    return to_ret

# Function to handle the "up" key press
def up():
    global index
    index -= 1
    if index < 0:
        index = index_max - 1

# Function to handle the "down" key press
def down():
    global index
    index += 1
    if index >= index_max:
        index = 0

# Function to handle the "enter" key press
def enter():
    global selected, index
    selected = index

# Function to display the menu options and handle user input
def display(options_json, color):
    last_known_index = 1
    
    global index, index_max, selected
    index = 0
    selected = None
    
    # Loop to continuously display the menu and wait for user input
    while True:
        if selected is not None:
            break
        if last_known_index != index:
            last_known_index = index
            cls()
            
            # Display menu options with highlighting for the selected option
            for i in range(index_max):
                if i == index:
                    print(color + options_json[i])
                else:
                    print(options_json[i])
    
    return options_json[selected]

# Example usage with test options (commented out for now)
test_options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
answer = create_menu(test_options, color=colorama.Fore.CYAN)
print(colorama.Fore.GREEN + f"Selected {answer}")