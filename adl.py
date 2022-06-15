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
<<<<<<< HEAD
    def __init__(self):         
            super().__init__(800,600, "UIFlatBUtton Example,",resizable=True)

            # ---Reuquired for all code that uses UI element,
            # a UIManager to handle the UI.
            self.manager = arcade.gui.UIManager()
            self.manager.enable()

            # Set background color
            arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

            # Create a vertical BoxGroup to align buttons
            self.v_box = arcade.gui.UIBoxLayout()

            # Create the buttons.
            start_button = arcade.gui.UIFlatButton(text= "Quit", width=200)
            self.v_box.add(quit_button.with_space_around(bottom=20))

            settings_button = arcade.gui.UIFlatButton(text="Settings", width=200)
            self.v_box.add(settings_button.with_space_around(bottom=20))

            # Again, method 1. Use a child class to handle events.
            quit_button = QuitButton(text="Start Game", width=200)
            self.v_box.add(quit_button)

            # --- Method 2 for handling click events,
            # assign self.on_click_start as callback
            start_button.on_click = self.on_click_start

            # --- Method 3 for handling click events,
            # use a decorator to handle on_click events
            @settings_button.event("on_click")
            def on_click_settings(event):
                print("Settings:", event)

            # Create a widget to hold the v_box widget, that will center the buttons
            self.manager.add(
                arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        ) 
     
def on_click_start(self, event):
            print("Start:", event)

def on_draw(self):
            self.clear()
            self.manager.draw()
=======
    def __init__(self):
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
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_start(self,event):
        print("Start:", event)

    def on_draw(self):
        self.clear()
        self.manager.draw()
>>>>>>> d730a498d6982480ca53a124ae2493228c8a28c4

window = MyWindow()

arcade.run()

import turtle, random
import winsound

pencere = turtle.Screen()
pencere.bgcolor('black')
pencere.title('Uzay savaşı')
pencere.bgpic('uzay.gif')
pencere.setup(width=600, height=600)

turtle.register_shape('oyuncu.gif')
turtle.register_shape('dusman.gif')
turtle.register_shape('ates.gif')

oyuncu = turtle.Turtle()
oyuncu.color('blue')
oyuncu.speed(0)
oyuncu.shape('oyuncu.gif')
oyuncu.setheading(90)
oyuncu.penup()
oyuncu.goto(0, -250)
oyuncuhizi = 20

ates = turtle.Turtle()
ates.color('yellow')
ates.speed(0)
ates.shape('ates.gif')
ates.setheading(90)
ates.penup()
ates.goto(0, -240)
ateshizi = 20
ates.hideturtle()
ates.turtlesize(1, 1)
ateskontrol = False

yaz = turtle.Turtle()
yaz.color('white')
yaz.speed(0)
yaz.penup()
yaz.goto(0, 200)
yaz.hideturtle()

def atesgit():
    y = ates.ycor()
    y = y + ateshizi
    ates.sety(y)
def sola_git():
        x = oyuncu.xcor()
        x = x - oyuncuhizi
        if x < -300:
         x = -300
        oyuncu.setx(x)
def saga_git():

    x = oyuncu.xcor()
    x = x + oyuncuhizi
    if x > 300:
        x = 300
    oyuncu.setx(x)
def yukari_git():
    y = oyuncu.ycor()
    y = y + oyuncuhizi
    if y > 270:
        y = 270
    oyuncu.sety(y)
def asagi_git():
    y = oyuncu.ycor()
    y = y - oyuncuhizi
    if y < -270:
        y = -270
    oyuncu.sety(y)

    x = oyuncu.xcor()
    x = x + oyuncuhizi
    if x > 300:
        x = 300
        oyuncu.setx(x)
def yukarı_git():
        y = oyuncu.ycor()
        y = y + oyuncuhizi
        if y > 270:
                y= -270
        oyuncu.sety(y)
def asagi_git():
                y = oyuncu.ycor()
                y = y - oyuncuhizi
                if y <-270:
                        y = -270
                oyuncu.sety(y)

def ateset():
        global ateskontrol
winsound.PlaySound('lazer.wav', winsound.SND_ASYNC)
x = oyuncu.xcor()
y = oyuncu.ycor() + 20
ates.goto(x, y)
ates.showturtle()
ateskontrol = True

hedefler = []
for i in range(8):
    hedefler.append(turtle.Turtle())
for hedef in hedefler:
     hedef.color('red')
     hedef.speed(0)
     hedef.turtlesize(1, 1)
     hedef.shape('dusman.gif')
     hedef.penup()
     hedef.setheading(90)
     x = random.randint(-280, 280)
     y = random.randint(180, 260)
     hedef.goto(x, y)


pencere.listen()
pencere.onkey(sola_git,'Left')
pencere.onkey(saga_git,'Right')
pencere.onkey(yukari_git,'Up')
pencere.onkey(asagi_git,'Down')
pencere.onkey(ateset, 'space')

while True:
    if ateskontrol:
        atesgit()
    for hedef in hedefler:
<<<<<<< HEAD
        y = hedef.ycor()
        y = y - 2
        hedef.sety(y)
        if hedef.distance(ates) < 20:
            ates.hideturtle()
            hedef.hideturtle()
            hedefler.pop(hedefler.index(hedef))
            winsound.PlaySound('patlama.wav', winsound.SND_ASYNC)
        if hedef.ycor() < -270 or hedef.distance(oyuncu) < 20:
            yaz.write('Maalesef, kaybettiniz!', align='center', font=('Courier', 24, 'bold'))
    if len(hedefler) == 0:
        yaz.write('Tebrikler, kazandınız!', align='center', font=('Courier', 24, 'bold'))   
=======
            y = hedef.ycor()
            y = y - 2
            hedef.sety(y)
            if hedef.distance(ates) < 20:
                ates.hideturtle()
                hedef.hideturtle()
                hedefler.pop(hedefler.index(hedef))
                winsound.PlaySound('patlama.wav', winsound.SND_ASYNC)

            if hedef.ycor() < -270 or hedef.distance(oyuncu) < 20:
                yaz.write('Maalesef, kabettiniz!', align='center', font=('Courier', 24, 'bold'))
>>>>>>> d730a498d6982480ca53a124ae2493228c8a28c4
