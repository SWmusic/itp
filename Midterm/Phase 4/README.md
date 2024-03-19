# I did a thing: Part 4, the finale

## What did I do?

I tiled phase 3 into a 20 x 20 grid pattern.

## How did I do it?

I added two for loops, the second one being nested within the first.

def draw():
  for x in range(0, 401, 20)
    drawObject(x, 0, .2)
    for y in range(0, 401, 20)
      drawObject(x, y, .2)

The first for loop changes the x variable. Because x is already defined as a variable within the function drawObject(x, y, s), we can have the computer count it. For the 20 x 20 grid option, I originally had for x in range(0, 401, 20):. This means the computer will count from 0, in increments of 20, to 400. The drawObject(x, 0, .2) combined with the for line means that the object I made will be drawn at a fifth of its original scale, every 20 pixels along the x axis in the positive direction and at 0 on the y axis (the top of Processing's graph).

In all honesty, I could've changed this to 0 to 381 and it still would've had the same effect I believe (upon testing this hypothesis, yes, it does, therefore I am keeping the change.). This works because processing prints the "tile" left to right, and up to down.

The second for loop (nested within the first) changes the y variable, while using the current x value. We can do this for the same reason we could do it to x, because it is already defined as a variable within the drawObject(x, y, s) function. For the 20 x 20 grid option, originally I had for y in range(0, 401, 20):. This means the computer will count from 0, in increments of 20, to 400. The drawObject(x, y, .2) combined with both for lines means that at the current x being counted, the object will be drawn at a fifth of its original scale every 20 pixels down along the y axis in the positive direction (because Processing's y axis is flipped from what we learned in school). This is how the 20 x 20 grid is formed.

At the time of this writing, the code currently looks like this:

def draw():
    for x in range(0, 381, 20):
        drawObject(x, 0, .2)
        for y in range(0, 381, 20):
            drawObject(x, y, .2)

## What did I struggle with, and how did I fix it?

At the start I did not nest for loops. This resulted in the drawing being printed only along the left and top side of the graph. The middle, right, and bottom were not filled with elden rings like I had hoped. Also, my first for loop was using the y axis, not the x. In hindsight, that last tidbit may not have mattered too much if I had coded it correctly, but I did not. My next failure resulted from starting with the y, not the x. I nested the for x loop within the y, but made the y variable a stagnant 0 instead of a variable. It looked something like this:

def draw():
  for y in range(0, 401, 80) # started 5 x 5 to test it
    drawObject(0, y, .8)
    for x in range(0, 401, 80)
      drawObject(x, 0, .8)

This resulted in the same image that was made at the start when I hadn't nested anything. After rereading the phase 4 section and more specifically, the for loop hint, I started with for x, nested the for y, and it resulted in the same image again! Oh, I need to make both position values variables. Then boom success. From there it was simple division to make sure they were the right size and would fit the graph correctly along the grid. Problem solved.

## Where did I get my code from?

I really only got the idea of the for loops from the midterm page. After writing out to myself how I wanted the drawings to be printed out I figured out the correct range and variable placements on my own. 
