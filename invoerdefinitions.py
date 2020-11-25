palette = {
    'white':color(248, 249, 250),
    'gray':color(233, 236, 239),
    'blue':color(234, 246, 253)
}

players = ['','','','']

def hover(a,b):
    isBetweenX = a[0] >= b[0] and a[0] <= b[0]+b[2]
    isBetweenY = a[1] >= b[1] and a[1] <= b[1]+b[3]
    if (isBetweenY and isBetweenX):
        return True
    return False

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
        text(join(self.text, ""), self.x + self.padding, self.y + self.h / 2)

    def hover(self):
        if hover([mouseX, mouseY],[self.x, self.y, self.w, self.h]):
            fill(palette['blue'])
            cursor(TEXT)
        else:
            fill(palette['white'])
            cursor(ARROW)
        if self.selected or (hover([mouseX,mouseY],[self.x,self.y,self.w,self.h]) and mouseButton == LEFT):
            fill(palette['gray'])
            self.selected = True