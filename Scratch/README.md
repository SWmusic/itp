# The Scratch Game Production Chronicles: (Next Triple A Title?)

## What I did!

I made a game in Scratch where you control a squirrel that's getting a crystal.

## How I did it!

### For the squirrel:

Using the given blocks, I set multiple threads that performed rotation and movement actions when pressing the up, down, left, or right arrow keys.
Also, once the squirrel reaches the sprite, "Crystal," I made it say "You win! Maybe?" to signify game over.

### For the crystal:

Using the blocks, I told the software that at the click of the green flag, the crystal displays the message, "Catch me in 7 seconds or else!" For 7 seconds.
If the squirrel touches the crystal in those 7 seconds, the crystal then makes the "collect" noise.
Dopamine production ensues.
If the squirrel fails to reach the crystal before the displayed message ends, then no collect sound is played.

## The trials and the tribulations:

Movement at first was only in the positive x-direction, no matter which arrow key pressed.
* By giving the command, "rotate x degrees," where x is a value of either -90, 0, 90, or 180, the squirrel would then rotate in the direction it would travel, thereby fixing that problem.

The crystal would not make the collect noise even after the pressing of the green flag, despite the sprite touching it.
* I learned that the pressing of the green flag does not start the game as a whole, rather, it just reads and performs any actions associated with it. Therefore, when I pressed the green flag and the sensor didn't detect the squirrel sprite touching the crystal, no noise would be made.
* To fix this, I added a display message to the crystal that says "Catch me in 7 seconds or else!" that lasts for 7 seconds to make it seem intentional that the sound wouldn't play if the fake time requirement was not met.

By changing the squirrel's win message from "You win!" to: "You win! Maybe?" It accounts for the fact that the player may not have reached the crystal in time.
* This gives the player the freedom to answer the existential crisis for themself, rather than have the computer do it for them.
* Good game design makes its players reflect on the experience and justify why they didn't reach the crystal in time.

## You reached the end!
