 # Interactive Python Menu

This Python script provides a simple interactive menu using the `keyboard` library. Users can navigate through the menu options using arrow keys and select an option by pressing Enter.
Keep in mind this project is simple and I probably won't care to fix errors but the issues tab is yours!
## Features

- Navigate through menu options using the arrow keys.
- Select an option by pressing `Enter` or the `right arrow` key.
- Cross-platform support for coloured output.

## Demo

![Example Video](https://github.com/Cloudzik1337/Interactive-Python-Menu/blob/main/showcase/y4k1yk.gif?raw=true)

## Usage

To use this interactive menu in your Python script, follow these steps:
1. Install the required libraries:
  ```bash
pip install colorama
pip install keyboard
```
2. Drag menu.py to your project:
3. Import menu.py and use `menu.Menu(options, color)` module
## Example
```python
import menu
import colorama

test_options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]

menu = menu.Menu(test_options, color=colorama.Fore.CYAN)

print(colorama.Fore.GREEN + f"Selected {menu.selected}")
  
```
## Plans
1. Add style presets
2. Center Menu (pystyle lib)
3. Find a way to only suppress arrow keys in the terminal not whole system
4. Make large options (>10) list split in half
5. Allow the user get the index number of user choice
6. Add proper exception handling

## License 
This project is licensed under the MIT License - see the LICENSE file for details.
