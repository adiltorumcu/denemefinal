"""
Example code showing how to create a button,
and the three ways to process button events.
"""
from turtle import width
from winreg import KEY_CREATE_SUB_KEY
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
    
    # --- Method 3 for handling click events,
    # use a decorator to handle on_click events
    @settings_button.event("on_click")
    def on_click_settings(event):
        print("Settings:", event)
    
    #Create a widget to hold the v_box widget, that will center the buttons
    self.manager.add(
        arcade.gui.UIAnchorWidget(
            anchor_x="center_x"
            anchor_y="center_y"
            child=self.v_box)
    )
  def on_click_start(self,event):
      print("Start:", event)

  def on_draw(self):
      self.clear()
      self.manager.draw()


window = MyWindow()
arcade.run()
import turtle
import random
import time 


pencere = turtle.Screen()
pencere.title("Dinosaur Game")
pencere.bgcolor("black")
pencere.setup(height=500, widht=800)
pencere.bgpic("back.gif")
pencere.tracer(0)

pencere.register_shape("dino.gif")
pencere.register_shape("cactus.gif")

dino = turtle.Turtle()
dino.spedd(0)
dino.shape("dino.gif")
dino.color("green")
dino.penup()
dino.dy = 0
dino.dx = 0
dino.state = "ready"
dino.height = 100
dino.width  = 120
dino.goto(-200, -50)

gravity = -0.5

kaktus = turtle.Turtle()
kaktus.speed(0)
kaktus.shape("cactus.gif")
kaktus.color("green")
kaktus.penup()
kaktus.dx = -5
kaktus.height = 60
kaktus.width = 28
kaktus.goto(200 ,-70)

def jump() :
    if dino.state == "ready":
        dino.dy = 12
        dino.state = "jumping"

pencere.listen()
pencere.onkeypress(jump,"space")

while True:
    time.sleep(0.01)
    if dino.ycor() < -50:
        dino.sety(-50)
        dino.dy=0
        dino.state="ready"

        if dino.ycor() != -50 and dino.state=="jumping":
            dino.dy+=gravity

        y=dino.ycor()
        y +=dino.dy
        dino.sety(y)
        x = kaktus.xcor()
        x +=kaktus.dx
        kaktus.setx(x)

        if kaktus.xcor() < -400:
            x = random.randint(400, 600)
            kaktus.setx(x)
            kaktus.dx *= 1.05 
        if  kaktus.distance(dino) < 30:
            print('GAME OVER')

        pencere.uptade()
        from tkinder import*