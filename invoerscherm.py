import invoerdefinitions as d

def setup():
    global screenSize
    global TextInput
    global Card
    size(d.screenSize[0], d.screenSize[1])
    background(color(255,255,255))
    TextInput = d.TextInput(0,160,400)
    for i in range(4):
        d.cards[i] = d.Card(i, d.screenSize[0]/2, 160, 400, 110, 10, 'white')
        d.cards[i].shadow(6, 1, 1)
        

def draw():
    d.drawCards()
    TextInput.draw()

def keyTyped():
    TextInput.addText(key)