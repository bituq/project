from functions import hover

cards = []

palette = {
           "red": color(249, 65, 68),
           "blue": color(87, 117, 144),
           "black": color(33, 37, 41),
           "white": color(255, 255, 255),
           "transparent": color(220,220,220,100),
           }

debounce = False

class Card:
    def __init__(self, card_color, index, Alpha):
        self.name = ""
        self.card_color = card_color
        self.index = index
        self.W = 400 #width
        self.H = 110 #height
        self.X = 300 #X position
        self.Y = 130 #Y position
        self.Spacing = 6 #Distance inbetween cards
        self.Bevel = 7 #Rounding of cards
        self.Alpha = Alpha #Transparency
        self.UnselectedFont = loadFont("SansSerif.plain-48.vlw")
    

    def draw_self(self, TextFieldHover = False, CardHover = False, Selected = False):
        Alpha = 255
        if self.card_color == "transparent":
            if CardHover == True:
                Alpha = 255
            else:
                Alpha = 140
        fill(palette[self.card_color])
        noStroke()
        rect(self.X, self.Y + (self.index * (self.H + self.Spacing)), self.W, self.H, self.Bevel)
        if TextFieldHover == True:
            fill(220,220,220,200)
        elif Selected == True:
            fill(240,240,240,200)
        else:
            fill(230,230,230,180)
        rect(self.X - self.X/4, self.Y + (self.index * (self.H + self.Spacing)), self.W/2, self.H/2, 3, 3, 0, 0)
        if TextFieldHover == True:
            stroke(40, 40, 40)
            strokeWeight(1)
        elif Selected == True:
            stroke(114, 9, 183)
            strokeWeight(1.5)
        else:
            stroke(80, 80, 80, 180)
            strokeWeight(1)
        strokeCap(SQUARE)
        line(self.X - 175, self.Y + (self.index * (self.H + self.Spacing)) + self.H/4, self.X + 25, self.Y + (self.index * (self.H + self.Spacing)) + self.H/4)
        fill(100,100,100,Alpha)
        textAlign(RIGHT, CENTER)
        textFont(self.UnselectedFont)
        textSize(18)
        text("Naam", self.X - self.X/4 - 40, self.Y + (self.index* (self.H + self.Spacing)))
            
        
        
    def draw_shadow(self, radius = 7):
        noStroke()
        r = radius
        offsetX = 0
        offsetY = 3
        fill(0,0,0,1)
        for i in range(120):
            rect(self.X + offsetX, self.Y + (self.index* (self.H + self.Spacing)) + offsetY, self.W + radius - i * .1, self.H + r - i * .1, self.Bevel)
