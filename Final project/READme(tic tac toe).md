# This is Sam's final project in LMSC-261!

## Really quickly before I do that!

This is a link to the repository/ folder of Pt. 2 of the project, the text adventure I made.

https://github.com/SWmusic/game-stuff/tree/main/1.%20Deepstone%20(WIP)

## Chronicle of everything I did to construct Tic Tac Toe.

Because this part of the project is following a video guide, I figured by detailing what I did and writing what my understanding of why everything was why it was would help you to see that I actually learned from this instead of just copying it. You will also see that I might've added extra stuff in to personalize my project a little more.

1. Using Shaun Halverson's video (https://www.youtube.com/watch?v=M3G1ZgOMFxo) as a guide, I began and made my tic tac toe.py file. We import the module, random.

2. I strayed off the path of the video a little by adding my own player_1_name variable. This asks for the player's name as a string input by the user. (note: mistake made, input function forgotten)

3. Made the arrays as per video instructions. The first array is 1 dimensional, the second is 2 dimensional, because of the second [] within a bracket [] like this: [[]].

4. Next we set up the rows and columns variables, where both = 3 because in basic tic tac toe lore there are 3 rows and 3 columns.

5. Here is where the printGameBoard function was made. It prints the current game board with the arrays.

6. A modifyArray function is made. For every possible choice by the player, the array is modified at the correct "place" on the board.

7. A while loop is made containing the turns for the player and the computer.

8. Pause video here, go over to Bro Code's youtube channel to learn about lists and 2d lists as I don't understand what Shaun is doing. (list/set/tuple = https://www.youtube.com/watch?v=gOMW_n2-2Mw&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=21

2d lists = https://www.youtube.com/watch?v=Xy6qeQWQwFw&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=23) UPDATE: I get it now!

9. numberPicked is an integer input from the user. We use this choice to modify the array, GameBoard. numberPicked only accepts numbers that are greater than or equal to 1, or less than or equal to 9. Any other input is invalid, and is asked to try again. Then the counter counts up 1, and because the new number on the counter is odd (or counter number % 2 =/= 1), it is now the cpu's turn.

10. The cpuChoice variable is a number equal to a randomly picked number from the possibleNumbers list. The computer then let's the player know what the cpu chose. The number on gameboard is then replaced with an 'O', and the number chosen from possibleNumbers is removed from the list. The turn counter goes up one, and because it is divisible by 2 again it is now player turn.

11. Now it's time for the computer to be able to check for winners. Because one symbol can win in 8 different ways (vertically on any column, horizontally on any row, or diagonally on either diagonal), there are 16 total combinations for both Os and Xs.

12. Finally, because the check_for_winner function returns a string, either 'X', 'O', or 'N', you must call the function at the end of the code, assign the output to a variable, in this case 'winner', and then check for what each possible output could be. For example, if winner == 'X', then print 'X has won!' and exit the program. Video finished!

## Troubleshooting Shaun's method

While the code is awesome and he explained things fairly well, there are some redundancies, and things that didn't work at first, even though I followed his code on the video and in his github project link (https://github.com/ShaunHalverson/PythonTicTacToe/blob/main/main.py), the game does not end even when the player can recognize a winner. So now, it is up to me to figure out this conundrum. First, I added elif statements checking for X and O as an output from the check_for_winner function. Originally, his code only checks for the output 'N'.

Because I am now delegating printing the win strings at the end, there was no need for the win strings in the check_for_winner function. This did not fix it. But I don't think it was a bad addition either.

To make the player go first, I made the while loop containing the statement: if(turnCounter % 2 == 1) change to being if(turnCounter % 2 == 0). This way since the turnCounter begins on 0, the player will go first since 0 % 2 = 0. Subsequently, the player 1 will have their turn on every even number. This is important later.

To fix the win condition, I figured that the computer needed to check for a winner every single turn after a certain point. There is no need to check for a winner at the start, as there will not have been enough moves to have anyone win. So, I put a while loop in the player 1 turn while loop, where while turnCounter >= 4 (4, because this means the player will have gone 3 times, enough to win). Success! But...

When you win, it prints x has won! Infinitely. How to fix? Let's find out. Well, by adding a break function inside the while loop, it stops printing infinitely. But, the game keeps going even while printing "x has won!". Even after adding exit functions won't exit even if the win condition is met.

Okay after contacting my friend from Texas, he told me to add from sys import exit, and to change my exit functions to exit(0) functions and boom. We have functional wins now.

Project complete!
