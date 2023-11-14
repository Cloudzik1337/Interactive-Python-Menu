 # Interactive Python Menu

This Python script provides a simple interactive menu using the `keyboard` library. Users can navigate through the menu options using arrow keys and select an option by pressing Enter.
Keep in mind this project is simple and I probably won't care to fix errors but the issues tab is yours!
## Features

- Navigate through menu options using the arrow keys.
- Select an option by pressing `Enter` or the `right arrow` key.
- Cross-platform support for coloured output.

## Demo
Show Case of each style first option is style number (1, 2, 11, 22)
![Example Video](https://github.com/Cloudzik1337/Interactive-Python-Menu/blob/main/showcase/bUZf5o.gif?raw=true)

## Usage

To use this interactive menu in your Python script, follow these steps:
1. Install the required libraries:
  ```bash
pip install keyboard (required)
pip install colorama (required for older versions > 1.0.2)
```
2. Drag menu.py to your project:
3. Import menu.py and use `menu.Menu(options, color)` module
## Example
```python
import menu


test_options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]

menu = menu.Menu(test_options, color='\033[36m'):  # Use ANSI escape code for color

print(colorama.Fore.GREEN + f"Selected {menu.selected}")
  
```
## Colors
|  FG |  BG | Color               |
|-----|-----|---------------------|
|  30 |  40 | Black               |
|  31 |  41 | Red                 |
|  32 |  42 | Green               |
|  33 |  43 | Yellow              |
|  34 |  44 | Blue                |
|  35 |  45 | Magenta             |
|  36 |  46 | Cyan                |
|  37 |  47 | White               |
|  90 | 100 | Bright Black (Gray) |
|  91 | 101 | Bright Red          |
|  92 | 102 | Bright Green        |
|  93 | 103 | Bright Yellow       |
|  94 | 104 | Bright Blue         |
|  95 | 105 | Bright Magenta      |
|  96 | 106 | Bright Cyan         |
|  97 | 107 | Bright White        |

So for example red would be `'\033[31m'`

## Plans
1. Add style presets
2. Center Menu (pystyle lib)
3. Find a way to only suppress arrow keys in the terminal not whole system
4. Make large options (>10) list split in half
5. Allow the user get the index number of user choice
6. Add proper exception handling

## License 
This project is licensed under the MIT License - see the LICENSE file for details.
