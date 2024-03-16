# POWER!!!!!!

## What I did to with this power:

I wrote a program that prints a graph of y = x^2 using *s. Oh, and it's horizontal.

## How I gained this power:

I basically said for x in range 8 to -9 (because of python's quirks with bound exclusivity) that y = x^2. Then, to print *s equal to the current y that is equal to the current x being raised to the power of 2.

## The struggles of gaining godhood (joke):

So at first it wouldn't print. I'm not quite sure why. I started it just simply by having the program print the answer to y = x^2, where a user input x just to make sure I was writing the power operator correctly. Then I switched to trying to write something.

At first I thought that maybe the templates provided might be mix and match, rather than pick one, but I knew I wanted a for loop similar to what was done with the pyramid problem. I tried defining a function, and then using the for loop attached to the equation (and print n number of stars for n number being counted for range n to n and blah blah blah), but even with the print command this didn't work. Then, I was like "oh I need to call the function again to make this do what I defined the function to do." But even after calling it, it didn't work. So I took a look at the code I had for the pyramid problem, and realized that I didn't need to define anything. I could simply just write a for a loop with a print command at the end.

Thus began the for loop problem. I feel like the pyramid problem was harder, and after gaining new insight to what the for loop could do numerically, it wasn't as hard to write the code this time! I already knew what I wanted it to do, which I think going forward will be key with any coding problem; I described to myself what was happening and how it was happening.

What was happening? - The computer is printing a y = x^2 graph horizontally. Each line is equal to the current number, x, being raised to the power of 2.

How was it happening? - Well, if each line is equal to the current number being squared, then I needed the computer to count and calculate at the same time. Thus, the for loop. By setting the range starting at 8, to -9 (because of bound exclusivity), and counting by -1 (8, -9, -1), then I could have the computer plug in the current number to the equation, then print * times the equation output, y.

Then, I wrote the ("*" 8 y, end=' ') and it printed the right amount, but it wasn't breaking to a completely new line, rather it was just breaking and then starting the new printing process. That's when I understood the purpose of including both end=' ' as a well as print(). By adding the final print() all was well in the world. And Sam saw that it was good. Thus began the 7th day of rest.

## Where did that code come from?

Well for once a lot of it came from my own brain. That being said, the idea stemmed from my friend's answer to the pyramid problem. I am gaining new understanding of the for loop. 
