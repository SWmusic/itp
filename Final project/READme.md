# This is Sam's final project in LMSC-261!

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
