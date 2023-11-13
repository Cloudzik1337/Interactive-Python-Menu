# Interactive Python Menu

This Python script provides a simple interactive menu using the `keyboard` library. Users can navigate through the menu options using arrow keys and select an option by pressing Enter.
Keep in mind this project is simple and probbably i wont care to fix errors but issues tab are yours!
## Features

- Navigate through menu options using the arrow keys.
- Select an option by pressing `Enter` or the `right arrow` key.
- Cross-platform support for colored output.

## Demo

![Example Video](https://raw.githubusercontent.com/your-username/your-repo/master/path/to/your/video/example.mp4)

## Usage

To use this interactive menu in your Python script, follow these steps:
1. Install the required libraries:
  ```bash
pip install colorama
pip install keyboard
```
2. Drag menu.py to your project:
3. Import menu.py and use `create_menu(options, color)` module
## Example
```python
import menu

test_options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]

answer = create_menu(test_options, color=colorama.Fore.CYAN)

print(colorama.Fore.GREEN + f"Selected {answer}")
  
```
## License 
This project is licensed under the MIT License - see the LICENSE file for details.
