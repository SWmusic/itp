# FizzBuzz and Pyramid! By Sam!

## Fizz! and Buzz!

### What I did:

I made a program that counts every number between 1 and 100. However, if the number it is counting is divisible by 3 and 5 cleanly, then instead of the integer, FizzBuzz is printed. If the number is only divisible cleanly by 3, then Fizz is instead printed, and finally, if the integer is only divisible by 5, then Buzz is printed.

### How I did it:

I wrote the range as being (1, 101). This way 1-100 is printed. I also set it to where it would count by 1, in the positive direction (1, 101, 1). Then, by writing if, elif, and else statements with each parameter explained in the what I did section, starting with the FizzBuzz input (important because if put last or in the middle some weird things might get printed), then going to the Fizz and Buzz sections of the code. The order of Fizz and Buzz does not matter as much, as long as they come after FizzBuzz, and are elif statements in comparison to FizzBuzz. Finally, I ended with an else statement, saying that if a number was counted that was not divisible by both or neither of those numbers, that it would simply print the number it's counting.

### Problems faced!

At first I wrote a good foundation using the for statement examples in the readme.md of the control flow folder in the class' github repository. However, I did not at first write the boolean statements associated with each condition. Of course every number is divisible by 3 and 5 if you don't care about the remainder! So I remembered to write the == for each one. Problem solved right? No. I was using the wrong operators. I had gotten // and % confused, especially with their relations to == 0. Once I had those switched, then all was well.

## Ooh pyramid ancient cool:

### What I did:

I wrote a program that makes a left-facing(?) pyramid constructed of #s, and the height is based off of an input by the user, that is an integer between 1 and 8.

### How I did it:

So I'm going to be honest. This is about half copied code. I understood well enough that making stacks a variable equal to an integer input by the user was the right way to go, as well as to write it like that. I also knew to write the if statement for if the number is outside the bounds we are looking for. The exit(1) was a reminder from my bro in Python that quitting the program was a valid command already built into the program. Lines 5-10 are his code. He told me that we could call so he could explain it to me, but we never ended up doing so within the due date, so in order to try and understand it, I drew out a diagram for myself on my Ipad, trying to explain each step to myself. In order to document best I can, I will write down my findings here so that my plagiarism at least shows a little bit of learning behind it.

### The vainglorious Ipad diagram:

So, stacks is a variable, an integer given to the program by the user specifically. The computer tells you that it must be between 1 and 8, and that it will create a pyramid as tall as the integer given. You will trust that the program can only make a pyramid between 1 and 8 tall. If you don't trust it, it will tell you YOU SHALL NOT PASS and you won't pass, just like me with this assignment. Then it will exit the program. It's not taking any orders anymore! Kitchen closed! However, if you did trust it, then it would go something like this:
Let's say the user put in 5. 5 is in between 1 and 8. The kitchen is NOT closed. Continue. F
or i in the range of 0 to 5 (stacks, the integer given by the user), which is 0, 1, 2, 3, and 4:
for j in range from 0, to 5-i (stacks minus the integers being counted from 0 to 5), which is 5-0, 5-1, 5-2, 5-3, and 5-4:
print a space, then end the line and continue printing spaces equal to the current place in the range.

" "" "" "" "" "

" "" "" "" "

" "" "" "

" "" "

" "

For k in range from 5 - i (stacks minus each integer being counted) to 5 + 1 (stacks + 1, 6): (5-4, 6)u(5-3, 6)u(5-2, 6)u(5-1, 6)u(5-0, 6)
print #s equal to the value of the integer being counted:

"#"

"#""#"

"#""#""#"

"#""#""#""#"

"#""#""#""#""#"

The spaces (being first in the control flow, and starting from large to small) push the #s right, forming the left facing pyramid produced by the code. Even with all this written out, I don't know that I follow the thought process behind it. I will ask for further guidance on this question. I'm too competitive to not want to know exactly how to solve this damn problem haha.

### The problems faced:

At first I had no idea how to start this besides asking for input and making a range that the program could operate in. To be fair, I still don't completely grasp why the for and range statements work and interact like they do, but that will be figured out at a later time. Not at 10:29PM on March 11, 2024. Perhaps the next day, where the author of this comically long documentation file can ask the teacher in person instead of relying on people who don't have PHDs in computer science and aren't really cool teachers by the name of Dr. Rome. Anyways, my first thought was to write if statements that would print the whole triangle, and to individually make a pyramid for each possible answer.
1) I knew this was lazy. What if the parameters weren't 1-8, but were 1-14 instead?
2) I knew there were more efficient ways of coding this out there, I just needed to find them (and understand them but I guess we can't have it all). Yrgos (probably spelled wrong) said he had solved it already. Why not ask him? Well he had an ingenious way of solving it: assign variables related to spaces and #s, and print based off the input given by the user. Awesome! Problem solved right? Nope, something was bugging me (pun intended). Ahh, no matter what number you put in, the #s always start pushed all the way to the right. But in the example, they slide over only as much as they need to. I need a different solution. I then had the idea to write using this foundation, but the equations themselves would change on each line. I was getting closer, right? No. I read the assignment again. There were hints of using for and range statements. But how? O woe, o woe is me.
I text my old friend Cameron, self taught coder. He solves it in maybe 2 minutes. But how? To quote,
"I used that at each step I wanted to print what I had left in the loop so I did stacks-i instead of i. I split the loops into one that prints spaces until stacks-i and one that print # from stacks-i to stacks+1. Had to do stacks+1 since python range is exclusive on the upper bound [lower,upper)."
To me saying I don't get it:
 "There was another approach with only one nested for loop (conditional). You can evaluate expressions within expressions is the key thing Im relying on. Stacks-i vs i is the difference between printing 1 # and printing 7 # for stacks=8. Gonna take a midterm rq but i can call you later if you want."
We never called :(. O the horror! Anyways, that's it for this document. As I am writing and rereading and rethinking more is making sense, but my brain is just on low power mode or something right now. Sorry for the long document!
