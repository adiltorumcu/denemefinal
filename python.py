"""
Example code showing how to create a button,
and the three ways to process button events.
"""
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

    