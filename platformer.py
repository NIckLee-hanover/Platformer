"""
platformer.py
Author: 
Credit: 
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""


from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

blue = Color(0x2EFEC8, 1.0)
black = Color(0x000000, 1.0)
pink = Color(0xFF00FF, 1.0)
red = Color(0xFF5733, 1.0)
white = Color(0xFFFFFF, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
grey = Color(0xC0C0C0, 1.0)

thinline = LineStyle(2, black)
blkline = LineStyle(1, black)
noline = LineStyle(0, white)
coolline = LineStyle(1, grey)
blueline = LineStyle(2, blue)
redline = LineStyle(1, red)
greenline = LineStyle(1, green)
gridline = LineStyle(1, grey)
grid = RectangleAsset(40,40,gridline,white)

#keys = ['up arrow', 'down arrow', 'right arrow', 'left arrow']
class Block(Sprite):
    grid = RectangleAsset(40,40,gridline,white)
    def __init__(self, position):
        super().__init__(Block.grid, position)
        Block.listenKeyEvent("mousedown", self.getmousepos)
    
    def getmousepos(self, event):
        self.mpx = round(round(event.x)/40)
        self.mpy = round(round(event.y)/40)
        
class Character(Sprite):
    Box = RectangleAsset(15, 25, noline, blue)
    def __init__(self, position):
        super().__init__(Character.Box, position)
        
        self.vx = 0
        self.vy = 0
        self.keydown = 0
        
        Platformer.listenKeyEvent("keyup", "up arrow", self.stop)
        Platformer.listenKeyEvent("keydown", "up arrow", self.up)
        Platformer.listenKeyEvent("keyup", "down arrow", self.stop)
        Platformer.listenKeyEvent("keydown", "down arrow", self.down)
        Platformer.listenKeyEvent("keyup", "right arrow", self.stop)
        Platformer.listenKeyEvent("keydown", "right arrow", self.right)
        Platformer.listenKeyEvent("keyup", "left arrow", self.stop)
        Platformer.listenKeyEvent("keydown", "left arrow", self.left)
        Platformer.listenMouseEvent("mousedown", self.yeet)
     
    def step(self):
        self.x += self.vx
        self.y += self.vy
        if self.keydown == 0:
            if round(self.vy, 3 == 5.551):
                self.vy = self.vy
            if self.vy != 0:
                if self.vy >= 0:
                    self.vy -= 0.2
                    if self.vy < 0.3:
                        self.vy = 0
                else:
                    self.vy += 0.2
                    if self.vy > -0.3:
                        self.vy = 0
                    
            if self.vx != 0:
                if self.vx >= 0:
                    self.vx -= 0.2
                    if self.vx < 0.3:
                        self.vx = 0
                else:
                    self.vx += 0.2
                    if self.vx > -0.3:
                        self.vx = 0
                    
    def down(self, event):
        self.keydown = 1
        if self.vy < 2:
            self.vy += 0.5
        
    def up(self, event):
        self.keydown = 1
        if self.vy > -2:
            self.vy -= 0.5
        
    def right(self, event):
        self.keydown = 1
        if self.vx < 2:
            self.vx += 0.5
        
    def left(self, event):
        self.keydown = 1
        if self.vx > -2:
            self.vx -= 0.5
        
    def stop(self, event):
        self.keydown = 0
    
    def yeet(self, event):
        ex = round(event.x)
        print(round(round(event.x)/40),round(round(event.y)/40))
        #print(((ex/40) - (ex % 40)), round(event.y))
        

        
    
class Platformer(App):
    global black, white, grey
    def __init__(self):
        super().__init__()
        noline = LineStyle(0, grey)
        bg_asset = RectangleAsset(self.width, self.height, noline, grey)
        bg = Sprite(bg_asset, (0,0))
        Character((100,100))

    
    def step(self):
        for Box in self.getSpritesbyClass(Character):
            Box.step()
        
class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self):
        super().__init__()
        
        # Background
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        SpaceShip((100,100))
        SpaceShip((150,150))
        SpaceShip((200,50))
        for i in range(0, (self.width/40)):
            grid((100,100))
        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()


myapp = Platformer()
myapp.run()












