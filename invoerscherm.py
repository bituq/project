import definitions as d

def setup():
    size(1080,720)
    background(color(255,255,255))
    global TextInput
    TextInput = d.TextInput(0,50,50)

def draw():
    TextInput.draw()

def keyTyped():
    TextInput.addText(key)