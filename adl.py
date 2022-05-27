"""
Example code showing how to create a button,
and the three ways to process button events.
"""
import arcade
import arcade.gui

# --- Method 1 for handling click events,
# Create a child class.
class QuitButton(arcade.gui.UIFlatButton) :
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()
