palette = {
    'white'         :   color(248, 249, 250),
    'gray'          :   color(233, 236, 239),
    'light_blue'    :   color(234, 246, 253),
    'blue'          :   color(87, 117, 144),
    'transparent'   :   color(220,220,220,100)
}

players = ['','','','']
cards = ['','','','']

screenSize = [1080, 720]

def hover(a,b):
    isBetweenX = a[0] >= b[0] and a[0] <= b[0]+b[2]
    isBetweenY = a[1] >= b[1] and a[1] <= b[1]+b[3]
    if (isBetweenY and isBetweenX):
        return True
    return False

def drawCards():
    global cards
    for i in range(4):
        try:
            cards[i].draw()
        except:
            print("ERROR: Could not draw card")


class Card:

    def __init__(self, index, x, y, w, h, spacing, cardColor):
        global players
        self.name = players[index]
        self.index = index
        self.cardColor = cardColor
        self.x = x              #   X position
        self.y = y              #   Y position
        self.w = w              #   Width
        self.h = h    
        self.spacing = spacing
        self.bevel = 7
    
    def draw(self):
        fill(palette[self.cardColor])
        #self.hover() # Make it so that self.hover() doesn't affect fill when not hovered.
        noStroke()
        rect(self.x, self.y + (self.index * ( self.h + self.spacing)), self.w, self.h, self.bevel)
    
    def shadow(self, radius, offsetX, offsetY, samples = 64):
        rectMode(CENTER)
        noStroke()
        fill(0,0,0,1)
        for i in range(samples):
            rect(self.x + offsetX, self.y + (self.index* (self.h + self.spacing)) + offsetY, self.w + radius - i * .1, self.h + radius - i * .1, self.bevel)


class TextInput:

    def __init__(self, index, x, y, w = 300 ,h = 50):
        self.x = x              #   X position
        self.y = y              #   Y position
        self.w = w              #   Width
        self.h = h              #   Height
        self.bevel = 6          #   Bevel
        self.padding = 15       #   Padding
        self.selected = False
        self.text = []
        self.debounce = False
        self.maxLength = 15
        self.index = index
        self.forbiddenKeys = [ENTER, TAB, BACKSPACE]
        fill(palette['white'])

    def draw(self):
        stroke(1)
        fill(255,255,255)
        rectMode(CENTER)
        self.hover()
        rect(self.x, self.y, self.w, self.h, self.bevel)
        self.displayText()

    def addText(self, input):
        if self.selected == True:
            if not input in self.forbiddenKeys and len(self.text) < self.maxLength:
                self.text.append(input)
            elif input == BACKSPACE:
                self.text = self.text[:len(self.text)-1]
            elif input == ENTER:
                global players
                temp = players[self.index]
                players[self.index] = join(self.text, "")
                print('Player ' + str(self.index) + '\'s name changed\nfrom: ' + temp + '\nto: ' + str(players[self.index]))

    def displayText(self):
        fill(0,0,0)
        textAlign(LEFT, CENTER)
        textSize(20)
        text(join(self.text, ""), self.x + self.padding - self.w / 2, self.y)

    def hover(self):
        if hover([mouseX, mouseY],[self.x, self.y, self.w, self.h]):
            fill(palette['light_blue'])
            cursor(TEXT)
        else:
            fill(palette['white'])
            cursor(ARROW)
        if self.selected or (hover([mouseX,mouseY],[self.x,self.y,self.w,self.h]) and mouseButton == LEFT):
            fill(palette['gray'])
            self.selected = True