 # Interactive Python Menu

This Python script provides a simple interactive menu using the `keyboard` library. Users can navigate through the menu options using arrow keys and select an option by pressing Enter.
Keep in mind this project is simple and I probably won't care to fix errors but the issues tab is yours!
## Features

- Navigate through menu options using the arrow keys.
- Select an option by pressing `Enter` or the `right arrow` key.
- Cross-platform support for coloured output.

## Demo
Show Case of each style first option is style number  Styles.<`DEFAULT, SELECTED, ARROW, CENTERED, CENTEREDSELECTED, ARROWCENTERED`>
![Example Video](https://github.com/Cloudzik1337/Interactive-Python-Menu/blob/main/showcase/1.0.4.gif?raw=true)

## Usage

To use this interactive menu in your Python script, follow these steps:
1. Install the required libraries:
  ```bash
pip install keyboard (required)
pip install pystyle (required for 1.0.3+)


pip install colorama (required ONLY for older versions > 1.0.2)

```
2. Drag menu.py to your project:
3. Import menu.py and use `ex_menu = menu.Menu(options, color=Colors.CYAN, style=Styles.DEFAULT, pretext=None)` module
4. `User_choice = ex_menu.launch(response="String")` # String Or index will be returned to User_choice var or just step 5
5. To get user selected input use menu.selected for str or menu.selected_index for index of options dict
## Example
```python
import menu


test_options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]

menu_ex = menu.Menu(test_options, color=Colors.CYAN, style=Styles.DEFAULT, pretext = None)  # Use Colors.<color>  for color and style = Syles.<style> For pretext take dump of your currently displayed cmd and provide content as string
User_choice = menu_ex.launch(response = "String") # can be String or Index its aditional if you use menu_ex.selected or menu_ex.selected_index you can replace this with menu_ex.launch()
print(menu.Colors.GREEN f"Selected {menu_ex.selected}, index = {menu_ex.selected_index}, {User_choice}")
  
```

## Plans
1. Add style presets ✔ Done
2. Center Menu (pystyle lib) ✔ Done
3. Find a way to only suppress arrow keys in the terminal not whole system ✘
4. Make large options (>10) list split in half ✘
5. Allow the user get the index number of user choice ✔ Done
6. Add proper exception handling ✘
7. Let user define text that would be printed before menu so it won't clear cmd ✔ Done

## License 
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Cloudzik1337/Interactive-Python-Menu/blob/main/LICENSE) file for details.
