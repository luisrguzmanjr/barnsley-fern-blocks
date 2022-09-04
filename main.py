def on_a_pressed():
    drawFern()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def drawFern():
    # initialize lists of x and y coordinates
    x = [0]
    y = [0]
    # initialize coordinate index
    for i in range(0, 99):
        # generating a random integer between 1 and 100
        z = randint(1, 100)
        # check the z range and append transformation to x and y coordinates
        if z == 1:
            x.append(0)
            y.append(0.16 * y[i])
        if z >= 2 and z <= 86:
            x.append(0.85 * x[i] + 0.04 * y[i])
            y.append(-0.04 * x[i] + 0.85 * y[i] +1.6)
        if z>= 87 and z<= 93:
            x.append(0.2 * x[i] - 0.26 * y[i])
            y.append(0.23 * x[i] + 0.22*(y[i])+1.6)
        if z >= 94 and z <= 100:
            x.append(-0.15 * x[i] + 0.28 * y[i])
            y.append(0.26 * x[i] + 0.24 * y[i] + 0.44)
    
    for i in range(x.length - 1):
        # map (x,y) to pixel coordinates
        ix, iy = width/2+x[i]*width/10, y[i]*height/12
        # draw green pixel point on the fern image
        fern.set_pixel(ix, iy, 7)
    pass
width = 100
height = 100
fern = image.create(width, height)
showFern = sprites.create(fern, SpriteKind.player)