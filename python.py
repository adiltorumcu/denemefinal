"""
Example code showing how to create a button,
and the three ways to process button events.
"""
from turtle import width
import arcade
import arcade.gui


#--- Method 1 for handling click events,
# Create a child class.
class QuitButton(arcade.gui.UIFlatButton) :
      def  on_click(self, event: arcade.gui.UIOnClickEvent) :
          arcade. exit() 


class MyWindow(arcade.Window):
    def_init_(self):
    super().__init__(800, 600, "UIFlatButton Example" , resizable=True)

    # --- Required for all code that uses UI element,
    # a UIManager to handle the UI.
    self.manager = arcade.gui.UIManager()
    self.manager.enable()

    # Set background color 
    arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

    # Create a vertical BoxGroup to align buttons
    self.v_box = arcade.gui.UIBoxLayout()
    
    # Create the buttons 
    start_button = arcade.gui.UIFlatButton(text="Quit",width=200)
    self.v_box.add(start_button.with_space_around(bottom=20))

    settings_button =arcade.gui.UIFlatButton(text="Settings" , width=200)
    self.v_box.add(settings_button.with_space_around(bottom=20))

    #Again,method 1. Use child class to handle events.
    quit_button = QuitButton(text="Start Game", width=200)
    self.v_box.add(quit_button)

    # --- Method 2 for handling click events,
    # assing self.on_click_start as callback
    start_button.on_click = self.on_click_start
    

