"""
Example code showing how to create a button,
and the three ways to process button events.
"""
import arcade
import arcade.gui


# --- Method 1 for handling click events,
# Create a child class.
class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()


class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "UIFlatButton Example", resizable=True)

                # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Set background color
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons
        start_button = arcade.gui.UIFlatButton(text="Quit Game", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))

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
def ateset():
    global ateskontrol
    winsound.PlaySound('lazer.wav', winsound.SND_ASYNC)
    x = oyuncu.xcor()
    y = oyuncu.ycor() + 20
    ates.goto(x, y)
    ates.showturtle()
    ateskontrol = True

durdur = False
def değiştir():
    global durdur
    if durdur == True:
        durdur = False
    else:
        durdur = True

if not durdur:
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
    pencere.onkey(değiştir , "p")

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

    import pygame
    import sys


# initializing the constructor
    pygame.init()

# screen resolution
    res = (720,720)

# opens up a window
    screen = pygame.display.set_mode(res)

# white color
    color = (255,255,255)

# light shade of the button
    color_light = (170,170,170)

# dark shade of the button
    color_dark = (100,100,100)

# stores the width of the
# screen into a variable
    width = screen.get_width()
# stores the height of the
# screen into a variable
    height = screen.get_height()

# defining a font
    smallfont = pygame.font.SysFont('Corbel',35)

# rendering a text written in
# this font
    text = smallfont.render('quit' , True , color)
    while True:

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()

        #checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            #if the mouse is clicked on the
            # button the game is terminated
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit()
