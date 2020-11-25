import invoerdefinitions as d

def setup():
    global screenSize
    global Card
    global TextInput
    size(d.screenSize[0], d.screenSize[1])
    background(color(255,255,255))
    for i in range(4):
        d.cards.append(d.Card(i, d.screenSize[0]/2, 160, 400, 110, 10, 'white'))
        d.textInputs.append(d.TextInput(i,d.cards[i].x,d.cards[i].y, 200))
        d.cards[i].shadow(6, 1, 1)
        

def draw():
    d.drawCards()

def keyTyped():
    for i in range(4):
        d.textInputs[i].addText(key)