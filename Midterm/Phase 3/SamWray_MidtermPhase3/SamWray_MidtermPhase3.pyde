def setup():
    size(400, 400)
    background(255)

def drawObject(x, y, s):
    push()
    translate(x, y)
    scale(s)
    noFill()
    ellipse(50, 60, 40, 40)
    ellipse(40, 70, 40, 40)
    ellipse(60, 70, 40, 40)
    ellipse(50, 50, 40, 40)
    line(50, 10, 50, 86)
    line(30, 0, 50, 10)
    line(50, 10, 70, 0)
    pop()

def draw():
    drawObject(0, 0, 1)
    drawObject(200, 200, 1)
    drawObject(100, 100, 1)
    drawObject(300, 300, 1)
    
    
